""" def check_valid_variable(variable):

    if variable.startswith('_'):
        return True
    if not variable[0].isdigit():
        # return True
        return 'Variable doesn\'t start with A Number' 
    if variable.startswith('@'):
        return 'Variable name doesn\'t starts with ' + variable[0]
    
    return variable """

# print(check_valid_variable('name'))

def check_valid_variable_2(variable, name):
    if variable.isidentifier():
        print(name.upper())
        return True 
    return False

while True: 
    value = input('Enter a variable name: ')
    if value == 'exit':
        break
    if check_valid_variable_2(value, 'variable'):
        print(f'The value {value} is valid.')
        break
    else:
        print(f'The value {value} is not valid.')


