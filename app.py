import pandas as pd 
import pickle 
from flask import Flask, request, jsonify 

app = Flask(__name__) 
model = pickle.load(open("model.pkl", "rb")) 
 
@app.route('/keepalive', methods=['GET']) 
def api_health(): 
    return jsonify(Message="Success") 
 
@app.route("/predict", methods=["POST"]) 
def predict(): 
    json_ = request.json 
    df = pd.DataFrame([json_])
    prediction = model.predict(df) 
    return jsonify({"Prediction": list(prediction)}) 
 
if __name__ == "__main__": 
    app.run(debug=True) 