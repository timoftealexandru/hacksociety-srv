from flask import Flask
from flask import request
from flask.wrappers import Response
import json
app = Flask(__name__)
from flask import send_file
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from camera import VideoCamera

cred = credentials.Certificate("firebase.json")
firebase = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://hacksociety-rpi.firebaseio.com'
})


@app.route('/', methods=['GET'])
def hello_world():
    ref = db.reference('data')
    print(ref.get())
    return Response(json.dumps(ref.get()), 200)

@app.route('/image', methods=['GET'])
def get_image():
    filename = 'img.jpg'
    return send_file(filename, mimetype='image/gif')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 ,debug=False)