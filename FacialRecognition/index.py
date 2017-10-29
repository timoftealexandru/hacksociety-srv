from flask import Flask
from flask import request
from flask.wrappers import Response
import json
app = Flask(__name__)
from flask import send_file
import time
from multiprocessing import Process, Value
import subprocess
import random
import os
import sys
sys.path.append(os.getcwd())

@app.route('/', methods=['GET'])
def index():
    return Response("good", 200)

@app.route('/stopVideo', methods=['GET'])
def stopVideo():
    return str(os.system("sudo service motion stop"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001 ,debug=False)
