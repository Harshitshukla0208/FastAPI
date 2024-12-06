# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:40:41 2020

@author: win10
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI, Query
import numpy as np
import pickle

# 2. Create the app object
app = FastAPI()
pickle_in = open("model.pkl", "rb")
classifier = pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
# @app.get('/{name}')
# def get_name(name: str):
#     return {'Welcome To Krish Youtube Channel': f'{name}'}

# 5. Expose the prediction functionality with required fields in query parameters
@app.get('/predict')
def predict_banknote(
    Accelerometer_1: float = Query(..., description="Value of Accelerometer_1"),
    Temperature: float = Query(..., description="Value of Temperature")
):
    # Predict using the model
    prediction = classifier.predict([[Accelerometer_1, Temperature]])
    
    # Convert the prediction (numpy.ndarray) to a Python list and return as JSON
    prediction_str = prediction  # Get the first element of the array

    return {
        'Accelerometer_1': Accelerometer_1,
        'Temperature': Temperature,
        'prediction': prediction_str
    }

# 6. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
