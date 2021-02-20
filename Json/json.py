# EX1

import Json


json_string = '{"name": "Ozone", "age": 20, "city": "Bnagkok"}'


python_dict = json.loads(json_string)


print(python_dict["name"])
print(python_dict["age"])
print(python_dict["city"])
