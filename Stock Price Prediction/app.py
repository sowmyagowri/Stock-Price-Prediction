from flask import Flask, render_template, request, make_response, url_for, flash, redirect, session, abort, jsonify,g
import json
from jsonschema import validate, ValidationError
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from functions import *
import  myexception

app = Flask(__name__)

auth = HTTPBasicAuth()

@app.errorhandler(myexception.MyExceptions)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

#home route
@app.route('/')
def index():
    return render_template('index.html')

#stock prices trend api
@app.route('/prediction', methods=['GET', 'POST'])
def get_prediction():
    
    try:
        if not request.json or not 'company' in request.json:
            abort(400)
        company = request.json['company']
        result = predict_prices(company)
        return jsonify(result)
    
    except ValidationError as e:
        raise myexception.CheckPostData("company data type is invalid, accepting string", 1)
    
if __name__ == '__main__':
    app.run(debug = True, host='localhost', threaded=True, port=50000)
