from flask import Flask
from modules.views import Directory
from flask import request, json
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
    random.choice([True, False])

    return ""


@app.route('/validate_background', methods=['POST'])
def return_contact_status():
    return ""


if __name__ == '__main__':
    app.run()