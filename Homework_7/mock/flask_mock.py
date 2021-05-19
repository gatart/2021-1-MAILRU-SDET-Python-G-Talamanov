import threading
import json
import requests

from flask import Flask, jsonify, request

import settings

app = Flask(__name__)

SURNAME_DATA = {}


@app.route('/get_surname/<name>', methods=['GET'])
def get_user_surname(name):
    surname = SURNAME_DATA.get(name)
    if surname:
        return jsonify(surname), 200
    else:
        return jsonify(f'Surname for user {name} not fount'), 404


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT
    })
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_mock()
    return jsonify(f'OK, exiting'), 200

# ------------------------------------My code-------------------------------------------------------------------------


@app.route('/del_surname/<name>', methods=['DELETE'])
def del_user_surname(name):
    surname = SURNAME_DATA.get(name)

    if surname:
        del SURNAME_DATA[name]
        return jsonify(f'{name} was successfully deleted'), 200
    else:
        return jsonify(f'User {name} does not have surname'), 404


@app.route('/put_surname/<name>', methods=['PUT'])
def put_user_surname(name):
    surname = json.loads(request.data)['surname']
    l_surname = SURNAME_DATA.get(name)

    SURNAME_DATA[name] = surname
    if l_surname:
        return jsonify(f'{name} was successfully updated'), 200
    else:
        requests.post(f'http://{settings.APP_HOST}:{settings.APP_PORT}/add_user', json={'name': name})
        return jsonify(f'User {name} was successfully added'), 201
