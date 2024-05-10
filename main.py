from flask import Flask, request
from flask_cors import CORS
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os
import io


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

class Predictor:
    def __init__(self):
        try:
            self.model = load_model("lenet_fyp.h5")
        except Exception as e:
            print(e)

    def model_predict(self, img_path):
        test_image = image.load_img(img_path, target_size=(128, 128))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = self.model.predict(test_image)
        return result

pre = Predictor()

class_labels = ['Non Demented', 'Mild Demented', 'Moderate Demented', 'Very Mild Demented']

@app.route('/')
def home():
    return "This is the server for FYP Project, Send request on /data endpoint to get result"

@app.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        img = io.BytesIO(img_bytes)
        result = pre.model_predict(img)
        predicted_class_index = np.argmax(result)
        predicted_class = class_labels[predicted_class_index]
        accuracy = np.max(result)
        accuracy = round(float(accuracy * 100), 2)
        return {'predicted_class': predicted_class, 'accuracy': accuracy}
    
    return "This is the server for FYP Project, Send request on /data endpoint to get result"

if __name__ == '__main__':
    app.run(debug=True)
