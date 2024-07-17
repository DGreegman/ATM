def add_number():
    num_one = int(input('Enter your first number'))
    num_two = int(input('Enter your second number'))
    sum = num_one + num_two
    return sum


def sub_number():
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
main()