from modules.exceptions import BadRequest
from modules.contact_statement import validate_contract, template_json
from modules.apis import Helpers
from random import randint
import datetime


class Directory:

    @staticmethod
    def insert_new_contact(request):
        # Parse JSON to object
        contact = request.get_json()

        # Validate request structure
        if not validate_contract(contact):
            raise BadRequest("Bad Request Error - Body "
                             "not satisfied the requirements", 4001)

        # Validate request body
        # Validate ID Type Provided
        doc_types = ['CC', 'TI', 'CE', 'PA', 'RC']

        doc_type = contact["id_type"]
        id_provided = contact["id"]
        expedition_date = contact["expedition_date"]

        if doc_type.upper() not in doc_types:
            raise BadRequest("Bad Request Error -  Id Type provided"
                             "doesn't exist in Colombia", 4002)

        # Validate content of ID provided
        if doc_type is 'CC' or 'TI' or 'RC':
            if not id_provided.isdigit():
                raise BadRequest("Bad Request Error -  Id provided doesn't match with the rules, please "
                                 "fill id value without special characters or letters", 4003)
        else:
            if id_provided.isalphnum() or id_provided.isdigit():
                raise BadRequest("Bad Request Error -  Id provided doesn't match with the rules, please fill id value"
                                 " without special characters", 4004)

        # Validate number of digits on ID
        if not 7 < len(id_provided) < 20:
            raise BadRequest("Bad Request Error -  The number of digits in id provided is suspect",
                             4005)

        # Validate expedition date of id
        try:
            date_time_obj = datetime.datetime.strptime(expedition_date, '%d/%m/%Y')
        except:
            raise BadRequest("Bad Request Error - The date provided not match with the format %d/%m/%Y", 4006)

        # 1st Step: Validate if the data filled is correct
        correct_data = Helpers.validate_data(contact)

        # 2nd Step: Validate contact Background
        contact_whitout_background = Helpers.validate_background(contact)

        # Proceed to 3th Step
        generated_response = {
            "Data correctly provided ": correct_data,
            "The user has no criminal record": contact_whitout_background
        }

        #  The contact must comply with the 2 previous steps to proceed to step 3
        if correct_data and contact_whitout_background:

            #  Score from Addi System
            threshold = 60
            random_number = addi_internal_validation()

            generated_response['Addi system score'] = random_number

            if random_number < threshold:
                generated_response["Result"] = "Success: The contact has met the requirements " \
                                               "to be on Addi directory"
            else:
                generated_response["Result"] = "Fail: The score obtained by the prospect does not meet the minimum" \
                                               " score, can not enter the directory"
        else:
            generated_response['Result'] = "Fail; The contact prospect does not meet the minimum requirements"

        return generated_response


@staticmethod
def addi_internal_validation():

    """
    Score classification service for future
    :param self:
    :param
    :return: Random number between 0 and 100
    """
    random_number = randint(0, 100)
    return random_number
