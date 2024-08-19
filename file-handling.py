import os
# location = '/test.txt'
""" file = open('./ATM/test.txt', 'r')
txt = file.readlines()
print(txt)
print(type(txt))
file.close() """

# with open('./ATM/test.txt', 'r') as file:
#     txt = file.readlines()
#     print(txt)
#     print(type(txt))

""" with open('./ATM/testss.txt', 'a') as file:
    file.write('This is a new line. in Tests filejdjdj') """

# try:
#     os.remove('./ATM/testss.txt')
# except FileNotFoundError:
#     print("The file does not exist")

if os.path.exists('./ATM/testss.txt'):
    print("Deleting File....")
    os.remove('./ATM/testss.txt')
    print("File deleted successfully")
else:
    print("The file does not exist")
