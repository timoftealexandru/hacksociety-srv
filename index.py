from flask import Flask
from flask import request
from flask.wrappers import Response
import json
app = Flask(__name__)
from flask import send_file
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time
from multiprocessing import Process, Value
import subprocess
import random
import os
import sys
sys.path.append(os.getcwd())
import motionmodule
import cameramodule
import tiltModule
import buzzModule
import temperatureModule
import rgbLedModule
#from camera import VideoCamera

cred = credentials.Certificate("firebase.json")
firebase = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://hacksociety-rpi.firebaseio.com'
})

def getTemperatureRange():
    ref=db.reference('temperatureRange')
    return ref.get()

def motionDetected(flag):
    ref = db.reference('motion')
    ref.update({
       'motionDetected': flag
    })

@app.route('/', methods=['GET'])
def index():
    ref = db.reference('data')
    getTemperatureRange()
    return Response(json.dumps(ref.get()), 200)

@app.route('/image', methods=['GET'])
def get_image():
    cam = cameramodule.cameramodule()
    return send_file(cam.takePicture(), mimetype='image/gif')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/startVideo', methods=['GET'])
def startVideo():
    return str(os.system("sudo service motion start"))

@app.route('/stopVideo', methods=['GET'])
def stopVideo():
    return str(os.system("sudo service motion stop"))
    
def updateTemp():
    print("TEMP")
    on = 'g'
    ref = db.reference('temperature')
    t = temperatureModule.temperature()
    temp = t.getTemperatureFormatted()
    ref.update({
       'current': temp
    })
    rng = getTemperatureRange()
    rgb = rgbLedModule.rgbModule()
    if (float(temp) < rng['min']):
        print("b")
        if (on != 'b'):
            rgb.turnOffLed(on)
        rgb.turnOnLed('b')
        on = 'b'
    elif (float(temp) >= rng['min'] and float(temp) < rng['max']):
        print("g")
        if (on != 'g'):
            rgb.turnOffLed(on)
        rgb.turnOnLed('g')
        on = 'g'
    else:
        print("r")
        if (on != 'r'):
            rgb.turnOffLed(on)
        rgb.turnOnLed('r')
        on = 'r'
    
def updateTilt():
    t = tiltModule.tilt()
    value = t.getValue()
    ref = db.reference('tilt')
    ref.update({
        'value': value
    })
    if (value == 1):
        b = buzzModule.buzz()
        b.start()
        time.sleep(1)
        b.stop()

def runLoopTemp():
    while True:
        updateTemp()

def runLoop():
    while True:
        updateTemp()
        m = motionmodule.motion()
        motionDetected(m.getValue())
        updateTilt()

if __name__ == '__main__':
    p = Process(target=runLoop)
    p2 = Process(target=runLoopTemp)
    p.start()
    p2.start()
    app.run(host='0.0.0.0', port=5000 ,debug=False)
    p.join()
    p2.join()