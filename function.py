def greeting():
    print("Hello World")
    print('Hello good afternoon')
    print('end of the function')

def main():
    greeting()
    print("Hello From main function")

# main() 
def get_full_name():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    full_name = first_name + " " + last_name
    print(full_name)

get_full_name() 

def add_number():
    num_one = int(input("Enter your first name: "))
    num_two = int(input("Enter your last name: "))
    sum = num_one + num_two
    
    print(sum)

# result = add_number()
# result = result + 500
# print(result) 

# RETURNING A VALUE TO A FUNCTION

def add_number():
    num_one = int(input("Enter your first number: "))
    num_two = int(input("Enter your second number: "))
    # sum = num_one + num_two
    # print(sum)
    return num_one * 10
    # print('returning sum of numbers')

# print(add_number())
result = add_number()
# print(result)

def multiplication(num):
    return num * 2
print(multiplication(result))