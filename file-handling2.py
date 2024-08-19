import json

person_dict = { 'name': 'John Doe', 'age': 30, 'city': 'New York'}

person2_dict = '''{
    "name": "Jane Doe",
    "age": "28",
    "city": "Los Angeles"
}'''

""" # convert to dictionary
person_data = json.loads(person2_dict)
print(type(person_data))
print(person_data)

# convert to json
person_json = json.dumps(person_dict)
print(type(person_json))
print(person_json) """

# create a new json file with dictionary
with open('./ATM/person-data.json', 'w', encoding='utf-8') as file:
    json.dump(person_dict, file, ensure_ascii=False, indent=4)