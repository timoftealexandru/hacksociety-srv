from flask import Flask
from flask.wrappers import Response
import json
app = Flask(__name__)
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("firebase.json")
firebase = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://hacksociety-rpi.firebaseio.com'
})


@app.route('/', methods=['GET'])
def hello_world():
    ref = db.reference('data')
    print(ref.get())
    return Response(json.dumps(ref.get()), 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)