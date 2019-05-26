from modules.exceptions import BadRequest
from modules.contact_statement import validate_contract, template_json
from modules.apis import Helpers


class Directory:
    @staticmethod
    def insert_new_contact(request):
        # Validate message Body
        request_body = request.get_json()
        if not validate_contract(request_body):
            raise BadRequest("Bad Request Error - Body "
                             "not satisfied the requirements", 4001)

        # Parse JSON to object


        # Validate message content


        #  Validate real Data


        #  Validate contact Background


        #  Score from Addi System
        threshold = 60
        random_number = Helpers.addi_internal_validation()

        if random_number < threshold:
            prospect = False
        else:
            prospect = True


        return "Hola"
