from flask import Flask
from flask import request
from flask import send_from_directory
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

pictures = [{'file' : 'notme.jpg', 'name' : 'Cristi'},{'file' : 'me2.jpg', 'name' : 'Tudor'},{'file' : 'me.jpg', 'name' : 'Tudor'}]

@app.route('/', methods=['GET'])
def index():
    return Response("good", 200)

@app.route('/base/<filename>', methods=['GET'])
def getStaticImage(filename):
    return send_from_directory(app.root_path + '/', filename)

@app.route('/compare', methods=['GET'])
def stopVideo():
	found = False
	foundItem = {'file' : "False", 'name' : "False"}
	for i in range(len(pictures)):
 		picture_of_me = face_recognition.load_image_file(pictures[i]['file'])
 		my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
 		urllib.request.urlretrieve("http://10.5.5.46:5000/base/img.jpg", "img.jpg")
	 	unknown_picture = face_recognition.load_image_file('img.jpg')
	 	unknown_face_encoding = face_recognition.face_encodings(unknown_picture)
	 	err = False
	 	if not (len(unknown_face_encoding) > 0):
	 		err = True
	 	if not err:
	 		results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding[0])
	 		if results[0] == True:
	 			found = True
	 			foundItem = pictures[i]

	if found == True:
	 	print("It's a picture of me!")
	else:
		print("It's not a picture of me!")
	return Response(json.dumps(foundItem), 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001 ,debug=False)
