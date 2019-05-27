
from modules.views import Directory
from flask import Flask, request, json
import random

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


@app.route('/directory/new_contact',  methods=['POST'])
def insert_new_contact():
    contact_validation = Directory.insert_new_contact(request=request)

    response = app.response_class(
        response=json.dumps(contact_validation),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/validate_data', methods=['POST'])
def validate_data():
    #modify_data = random.choice([True, False])
    modify_data = True
    if modify_data:
        contract = request.data.get
        resp = {"background": modify_data}
    else:
        resp = {"background": modify_data}

    response = app.response_class(
        response=json.dumps(),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/validate_background', methods=['POST'])
def return_background():
    has_background = random.choice([True, False])
    response = app.response_class(
        response=json.dumps({"background": has_background}),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run()