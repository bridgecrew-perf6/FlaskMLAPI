import flask
from flask import Flask, jsonify, request
import json
import pickle

def load_models():
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

app = Flask(__name__)
@app.route('/predict', methods=['GET'])
def predict():
    # Stub input features
    x = 5.963

    # load model
    model = load_models()
    prediction = model.predict([[x]])

    response = json.dumps({'response': prediction[0]})
    return response, 200

if __name__ == '__main__':
    application.run(debug=True)