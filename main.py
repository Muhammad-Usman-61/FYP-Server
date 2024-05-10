from flask import Flask, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np


app = Flask(__name__)

@app.route('/')
def home():
    return "This is the server for FYP Project, Send request on /data endpoint to get result"

@app.route('/data', methods=['POST', 'GET'])
def data():
    return "This is the server for FYP Project, Send request on /data endpoint to get result"


if __name__ == '__main__':
    app.run(debug=True)
