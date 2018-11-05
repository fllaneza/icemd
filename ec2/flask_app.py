import numpy as np
import pandas as pd
from sklearn.externals import joblib
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    json_ = request.json
    query = pd.DataFrame(json_).values
    prediction = regr.predict(query)
    return jsonify({'prediction': list(prediction)})
    
if __name__ == '__main__':
    regr = joblib.load('model.pkl')
    app.run(port=8080)
