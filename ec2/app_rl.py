import pandas as pd
from sklearn.externals import joblib
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    test_json = request.get_json()
    query = pd.read_json(test_json, orient = 'records')
    prediction = regr.predict(query)
    return jsonify({'prediction': list(prediction)})
    
if __name__ == '__main__':
    regr = joblib.load('model.pkl')
    app.run(host="0.0.0.0", port=80)
