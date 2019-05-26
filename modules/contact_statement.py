
template_json = {
                 "id_type": "",
                 "id": "",
                 "expedition_date":"",
                 "first_names": "",
                 "second_names": "",
                 "phone_number": "",
                 "home_address": "",
                 "city": "",
                 "email": "",
                 }

example_template = {
        "id_type": "cc",
        "id": "asdasd",
        "expedition_date": "25/09/2009",
        "first_names": "Adriana Fernanda",
        "second_names": "Moya Forero",
        "phone_number": "31456788",
        "home_address": "Cra 1 # 1-01 Bog",
        "city": "Bogotá",
        "email": "abc@test.co",
}


def validate_contract(request):
    try:
        assert template_json.keys() == request.keys()
        return True
    except AssertionError:
        return False
