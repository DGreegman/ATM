my_dict = {
    "firstname": "Gracious",
    "lastname": "John",
    "skills": ['html', 'JavaScript', 'Python', 'Typescript'],
    "12": 18,
    "address": {
        "street": 123 ,
        "city": "New York",
        "state": "NY",
        "zip_code": "10001",
        'type': 'dict'
    }
}
# print(my_dict.get(12))
my_dict["firstname"] = 'Hello World'
print(my_dict.get("firstname"))
key = input('Enter a random key ')
if my_dict.get(key):
    print(my_dict.get(key))
else: 
    print('Does not exist')
# print(my_dict)
# print(my_dict['name'])
""" print(my_dict["address"]['zip_code'])
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
print(my_dict['skills']) """

""" print('names' in my_dict)
my_dict.pop('name')
print(my_dict.get('name'))
my_dict.popitem()
print(my_dict) """
# print(my_dict)

""" for key, value in my_dict.items():
    print(f'{key}--{value}') """

""" for value in my_dict:
    print(value)

copied_dict = my_dict.copy()
print(copied_dict) """  

""" print(my_dict.keys())
print(my_dict.values()) """
   

