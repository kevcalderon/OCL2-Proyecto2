from flask import Flask, jsonify, request, Response
from flask_cors import CORS

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
    print(params)
    response = {'message': 'success'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)