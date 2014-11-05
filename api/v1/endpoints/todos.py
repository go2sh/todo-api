from flask import  jsonify

from api.v1 import api

@api.route('/todos')
def get_todos():
    todos = ['eins','zwei']
    return jsonify(todos)
