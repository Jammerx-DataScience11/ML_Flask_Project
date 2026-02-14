from flask import Flask , request , jsonify
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl' , 'rb'))

@app.route("/" )
def home():
    return "ML model is running sucessfully"

@app.route("/predict" , methods = ["POST"])
def predict() : 
    data = request.json["value"]
    prediction = model.predict(([[data]]))
    return jsonify({"prediction" : prediction.tolist()})

if __name__ == "__main__" : 
    app.run(debug = True)


