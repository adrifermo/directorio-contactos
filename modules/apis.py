import random
import json,requests
from modules.exceptions import BadRequest


class Helpers:
    @staticmethod
    def validate_data(contact):
        try:
            url = "http://localhost:5000/validate_data"
            data = json.dumps(contact)
            result = requests.post(url, data=data)
            response = json.loads(result.text)
            return response['background']
        except:
            raise BadRequest("Was not possible to connect to the API", 4007)

    @staticmethod
    def validate_background(contact):
        try:
            url = "http://localhost:5000/validate_background"
            data = json.dumps(contact)
            result = requests.post(url, data=data)
            response = json.loads(result.text)
            return response['background']
        except:
            raise BadRequest("Was not possible to connect to the API", 4007)

