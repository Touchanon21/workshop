import json


python_dict = {
    "name": "Ozone",
    "age": 20,
    "city": "Bnagkok"
}


json_string = json.dumps(python_dict)


print(json_string)
