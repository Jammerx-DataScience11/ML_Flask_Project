from flask import Flask , request , jsonify
from functools import wraps
import numpy as np
import pickle
import os


app = Flask(__name__)
## Implementing API Key-BAsed Authentication in Flask
## creating an API key for testing 

API_KEY = os.getenv("API_KEY") 

## creating authentication decorator 


def require_api_key(f) : 
    @wraps(f)
    def wrapper(*args , **kwargs) : 
          key = request.headers.get("x-api-key")
          if key and key == API_KEY : 
              return f(*args , **kwargs)
          else : 
              return jsonify({"error" : "Unauthorised access"}) , 401
          
          
          
    return wrapper
    



model = pickle.load(open('model.pkl' , 'rb'))

@app.route("/" )
def home():
    return "ML model is running sucessfully"

@app.route("/predict" , methods = ["POST"])
@require_api_key  # middleware/guard to protect the endpoint with API key authentication
def predict() : 
    data = request.json["value"]
    prediction = model.predict(([[data]]))
    return jsonify({"prediction" : prediction.tolist()})

if __name__ == "__main__" : 
    app.run(debug = True)


