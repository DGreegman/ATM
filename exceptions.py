""" try:
    print(10 + '5' )
except:
    print('TypeError: cannot convert integer to to a string') """

# print(10 / 0 )

""" try:
    name = input('Enter your Name')
    year_of_birth = input('Year of Birth')
    year_of_birth = int(year_of_birth)

    age = 2024 / year_of_birth
    print(f'Hello {name}, you are {age} years old.')
except TypeError:
    print('Type Error occurred')
except ValueError:
    print('Invalid Year of Birth')
except ZeroDivisionError:
    print('Zero division error occurred') """

""" num_1 = int(input('Enter Num one '))
num_2 = int(input('Enter Num two '))

try:
    result = num_1 / num_2
    print(f'Result: {result}')
except ZeroDivisionError:
    print('Error: Division by zero is not allowed.') """

try:
    # name = 'John Doe'
    num_1 = int(input('Enter First Number:'))
    num_2 = int(input('Enter Second Number:'))
    
    # print(num_1 + num_2)
    print(num_1 / num_2)
except ZeroDivisionError:
    print('Error: Division by zero is not allowed')
except Exception as e:
    print(e)
finally:
    print('Finally block executed')
                          