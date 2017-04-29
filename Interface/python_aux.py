#!flask/bin/python
from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request
from flask import abort
from flask_cors import CORS, cross_origin

#any other imports
from compiler_connection import Compiler_Handler

compiler_handler = Compiler_Handler()

app = Flask(__name__)
CORS(app)

code_js = []
result = []

@app.route('/post_code', methods=['POST'])
def compile_code():
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

@app.route('/compile', methods=['GET'])
def get_names():
    if not code_js:
        return jsonify({'code': "EMPTY"})

    else:
        #compile and update data in class
        compiler_handler.compile(code_js)
        return jsonify({'result': compiler_handler.result})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)

"""
@app.route('/names/<int:index>', methods=['GET'])
def get_name(index):
    name = things[index]
    if index < 0:
        abort(404)
    return jsonify({'name': name })

@app.route('/names', methods=['POST'])
def create_name():
    #json error
    if not request.json or not 'name1' in request.json:
        abort(400)
    name1 = request.json['name1']

    things.append(name1)

    return jsonify({'new name list': things}), 201

@app.route('/names/<int:id>', methods=['PUT'])
def update_name(id):
    task = things[id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != unicode:
        abort(400)
    #in case it doesn't receive parameter it repeats name
    things[id] = task + request.json.get('name', task)
    return jsonify({'updated name': things[id]})
    """