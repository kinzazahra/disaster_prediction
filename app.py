from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
import numpy as np
from utils.map_utils import create_map

app = Flask(__name__)

# Load model
model = pickle.load(open('model/model.pkl', 'rb'))

@app.route('/')
def home():
    data = pd.read_csv('data/dataset.csv')
    map_html = create_map(data)
    return render_template('index.html', map=map_html)

# 🔥 NEW ROUTE
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    features = np.array([[ 
        float(data['rainfall']), 
        float(data['slope']), 
        float(data['elevation'])
    ]])

    prediction = model.predict(features)[0]

    return jsonify({
        "risk": int(prediction)
    })

if __name__ == '__main__':
    app.run(debug=True)