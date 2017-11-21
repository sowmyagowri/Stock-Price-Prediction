from flask import Flask, render_template, request, make_response, url_for, flash, redirect, session, abort, jsonify,g
import json
from jsonschema import validate, ValidationError
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
#from functions import *
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
def get_historical():
    
    try:
        quote = request.json['company']
        # Download our file from google finance
        url = 'http://www.google.com/finance/historical?q=NASDAQ%3A'+quote+'&output=csv'
        r = requests.get(url, stream=True)
    
        dataset = []
    
        with open(FILE_NAME) as f:
            for n, line in enumerate(f):
                if n != 0:
                    dataset.append(float(line.split(',')[1]))
    
        dataset = np.array(dataset)
    
        # Create dataset matrix (X=t and Y=t+1)
        dataX = [dataset[n+1] for n in range(len(dataset)-2)]
        trainX = np.array(dataX)
        trainY = dataset[2:]
    
        # Create and fit Multilinear Perceptron model
        model = Sequential()
        model.add(Dense(8, input_dim=1, activation='relu'))
        model.add(Dense(1))
        model.compile(loss='mean_squared_error', optimizer='adam')
        model.fit(trainX, trainY, nb_epoch=200, batch_size=2, verbose=2)
    
        # Our prediction for tomorrow
        prediction = model.predict(np.array([dataset[0]]))
        result = 'The price will move from %s to %s' % (dataset[0], prediction[0][0])
        
        return jsonify(result)
    
    except ValidationError as e:
        raise myexception.CheckPostData("company data type is invalid, accepting string", 1)
    
if __name__ == '__main__':
    app.run(debug = True, host='localhost', threaded=True, port=50000)
