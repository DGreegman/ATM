my_dict = {
    "name": "Gracious",
    "lastname": "John",
    "skills": ['html', 'JavaScript', 'Python', 'Typescript'],
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY",
        "zip_code": "10001",
        'type': 'dict'
    }
}
# print(my_dict['name'])
print(my_dict["address"]['zip_code'])
print(my_dict['skills'][1])
print(len(my_dict))
print(type(my_dict['skills'][0]))

if my_dict.get('firstname'):
    print('Name exists in the dictionary')
else:
    print('Name does not exist in the dictionary')
print(my_dict.get('name'))

my_dict['name'] = 'testing'
my_dict['skills'].insert(2, 'Go lang')
# my_dict['skills'].clear()
print(my_dict['skills'])

print('names' in my_dict)
my_dict.pop('name')
print(my_dict.get('name'))
# print(my_dict)

