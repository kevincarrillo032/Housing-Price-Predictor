# -*- coding: utf-8 -*-
"""app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pZGa7ODb8GYiSnG2Sg76uxoHQMXP3vdZ
"""

from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the model
model = joblib.load('random_forest_model.pkl')

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    data = request.form
    features = np.array([[
        float(data['sqft_living']),
        float(data['grade']),
        float(data['bathrooms']),
        float(data['bedrooms']),
        int(data['waterfront']),
        int(data['view']),
        float(data['floors']),
        int(data['condition']),
        float(data['lat']),
        float(data['long']),
        int(data['location_cluster']),
        int(data['renovated']),
        int(data['yr_built'])
    ]])

    # Predict the price
    prediction = model.predict(features)[0]

    # Return the prediction as JSON
    return jsonify({'predicted_price': round(prediction, 2)})

if __name__ == '__main__':
    app.run(debug=True)