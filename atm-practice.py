balance = 1000

# adding to the balance 

choice = int(input('How much do you want to add to the balance'))

if choice <= 0:
    print('Invalid amount')

else:
    balance += choice
    # balance = balance + choice 
    print(f'Your new balance is now: ${balance}')

# widtrawing from the balance

choice = int(input('How much do you want to widthdraw from the balance '))

if choice <= 0 or choice > balance:
    print('Invalid amount or insufficient balance')

else:
    balance -= choice
    # balance = balance - choice
    print(f'Your new balance is now: ${balance}')


# checking the balance

# print(f'Your current balance is: ${balance}')