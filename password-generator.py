import random 
print("Welcome to Your Password")
print("========================")
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$^%&*(),.?0123456789"
# print(len(characters))
number = input("Enter The Amount of Passwords to Generate...")
number = int(number)
length = input("Input Your Password Length")
length = int(length)
print("Here are Your Passwords: ")

for pwd in range(number):
    passwords = ""
    for chars in range(length):
        passwords += random.choice(characters)
    print(passwords)