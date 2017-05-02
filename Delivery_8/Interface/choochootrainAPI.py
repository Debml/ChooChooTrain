#!flask/bin/python
from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request
from flask import abort
from flask_cors import CORS, cross_origin

#any other imports
from compiler_connection import Compiler_Handler

app = Flask(__name__)
CORS(app)

code_js = []
result = []
user_input = []

#compiler handler
compiler_handler = Compiler_Handler()

@app.route('/post_code', methods=['POST'])
def post_code():
    #json error
    if not request.json or not 'code' in request.json:
        #abort(400)
        result_code = 400;

    else:
        #reset code stored and store new
        if code_js:
            code_js.pop()

        code_js.append(request.json['code']);
        #operation successful
        result_code = "1"

    return jsonify({'result': result_code}), 201

@app.route('/post_input', methods=['POST'])
def post_user_input():
    #json error
    if not request.json or not 'user_input' in request.json:
        #abort(400)
        result_code = 400;

    else:
        #reset code stored and store new
        if user_input:
            user_input.pop()

        user_input.append(request.json['user_input']);
        #send input to handler and receive result
        result_code = compiler_handler.send_input(user_input[0])

    return jsonify({'result': result_code}), 201

@app.route('/get_code', methods=['GET'])
def get_code():
    if not code_js:
        return jsonify({'code': "EMPTY"})

    else:
        return jsonify({'code': code_js[0]})

@app.route('/compile', methods=['GET'])
def compile():
    if not code_js:
        return jsonify({'code': "EMPTY"})

    else:
        #compile and update data in class
        result = compiler_handler.compile(code_js[0])
        return jsonify({'result': result})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)