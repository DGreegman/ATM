def add_number(num_one, num_two, num_three):
    sum = f'{num_one  + num_two +num_three}'
    return num_one * 100

num_1 = int(input('enter number one'))
num_2 = int(input('enter number number two'))
num_3 = int(input('enter number number three'))
print(add_number(num_1, num_2, num_3))
""" 

# print(add_number(7, 20))

def greeting(num_1, num_2):
    return f'Hello {name}-{message}'


print(greeting()) """

""" def sub_number():
    num_one = int(input('Enter your first number'))
    num_two = int(input('Enter your second number'))
    diff = num_one - num_two
    return diff

def mul_number():
    num_one = int(input('Enter your first number'))
    num_two = int(input('Enter your second number'))
    product = num_one * num_two
    return product

def div_number():
    num_one = int(input('Enter your first number'))
    num_two = int(input('Enter your second number'))
    quotient = num_one / num_two
    return quotient

def breakpoint():
    print('Are you sure you want to exit?...')
    print('Yes, exit\nNo to continue')
    choice = input('Enter your choice')
    if choice == 'Yes':
        exit()



def main():
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    while True:
        choice = int(input('Enter your choice '))
        if choice > 4:
            print('Invalid choice')
            break
        if choice == 0:
            breakpoint()
        if choice == 1:
            print(add_number())
        elif choice == 2:
            print(sub_number())
        elif choice == 3:
            print(mul_number())
        elif choice == 4:
            print(div_number())
main() """