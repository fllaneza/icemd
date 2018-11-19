import pandas as pd
from sklearn.externals import joblib
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            data = request.get_json()
            query = pd.DataFrame.from_dict(data['json_request'])
            lin_reg = joblib.load('./model.pkl')
        except ValueError:
            return jsonify("Input error")
        
        return jsonify(lin_reg.predict(query).tolist())
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 9999)



