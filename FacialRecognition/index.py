from flask import Flask
from flask import request
from flask.wrappers import Response
import json
app = Flask(__name__)
from flask import send_file
import time

import urllib.request

from multiprocessing import Process, Value
import subprocess
import random
import os
import sys
sys.path.append(os.getcwd())
import face_recognition

@app.route('/', methods=['GET'])
def index():
    return Response("good", 200)

@app.route('/compare', methods=['GET'])
def stopVideo():
    picture_of_me = face_recognition.load_image_file("me2.jpg")
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

    urllib.request.urlretrieve("http://10.5.5.46:5000/base/img.jpg", "img.jpg")

    unknown_picture = face_recognition.load_image_file("img.jpg")
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)

    if not len(unknown_face_encoding) > 0:
        return "False"

    results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding[0])

    if results[0] == True:
        print("It's a picture of me!")
    else:
        print("It's not a picture of me!")
    return str(results[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001 ,debug=False)
