from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from controllerAlgorithm import *
import pandas as pd
from io import StringIO
from globalArray import graphArray

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/graph', methods=['GET'])
def getGraph():
    drawResponse = graphArray[-1]
    output = io.BytesIO()
    FigureCanvas(drawResponse).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


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
        response = {'RMSE': regresion[0], "R2": regresion[1], "Predicción": regresion[2], "graph": "true"}
        return jsonify(response)
    elif typeAlgorithm == "2":
        regresion = regresionPolinomial(param1, param2, predi,data)
        response = {'RMSE': regresion[0], "R2": regresion[1], "Predicción": regresion[2], "graph": "true"}
        return jsonify(response)
    elif typeAlgorithm == "3":
        clasificadorGaussiano(param1,param2,predi,data)
        response = {'message': 'success'}
        return jsonify(response)
    elif typeAlgorithm == "4":
        arbol = arbolDecision(param1,param2,predi,data)
        # print("RESPUESTA1",arbol[0])
        # print("RESPUESTA2",arbol[1])
        
        response = {"Prediccion": float(arbol[0]), "Acurracy": float(arbol[1]), "graph": "true"}
        return jsonify(response)
        # response = {'message': 'success'}
        # return jsonify(response)
    elif typeAlgorithm == "5":
        redesNeuronales(param1,param2,predi,data)
        response = {'message': 'success'}
        return jsonify(response)



if __name__ == '__main__':
    # from waitress import serve
    # serve(app, port=5000)
    app.run(debug=True)