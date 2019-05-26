from flask import Flask
from modules.views import Directory
from flask import request

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


@app.route('/directory/new_contact',  methods=['POST'])
def insert_new_contact():

    contact = Directory.insert_new_contact(request=request)

    return ""


@app.route('/directory/list_contacts', methods=['POST'])
def list_contacts():
    return ""


@app.route('/directory/return_contact_status', methods=['POST'])
def return_contact_status():
    return ""


if __name__ == '__main__':
    app.run()