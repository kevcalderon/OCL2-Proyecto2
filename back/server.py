from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from controllerAlgorithm import *
import pandas as pd
from io import StringIO

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/getFile', methods=['GET'])
def getFile():
    response = {'message': 'success'}
    return jsonify(response)

@app.route('/api/v1/users/<id>', methods=['GET'])
def get_user(id):
    response = {'message': 'success'}
    return jsonify(response)

@app.route('/read', methods=['POST'])
def readFile():
    params = request.get_json(force =True)
    
    # obtener el tipo de algoritmo
    typeAlgorithm = params['algoritmo']
    param1 = params['param1']
    param2 = params['param2']
    predi = params['predi']
    
    # obtener la info del archivo y utilizar pandas para leerlo
    inputFile = StringIO(params['inputFile'])
    data = pd.read_csv(inputFile)
    # print(data)
    if typeAlgorithm == "1":
        regresion = regresionLineal(param1, param2, predi,data)     
        response = {'RMSE': regresion[0], "R2": regresion[1], "Predi": regresion[2]}
        return jsonify(response)

    elif typeAlgorithm == "2":
        regresionPolinomial(param1, param2, predi,data)
    elif typeAlgorithm == "3":
        clasificadorGaussiano()
    # response = {'message': 'success'}
    # return jsonify(response)

@app.route('/graph', methods=['GET'])
def getGraph():
    response = {'message': 'sucess'}
    return jsonify(response)

if __name__ == '__main__':
    # from waitress import serve
    # serve(app, port=5000)
    app.run(debug=True)