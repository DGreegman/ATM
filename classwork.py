fruits = {'apple', 'orange', 'banana', 'pinanapple', 'cherry', 'rose', 'chinelo', 'Jefery', 'cucumber', 'carrot'}
def check_set():
    copy_fruits = set()
    user_fruit = input('Please input a fruit name')
    if user_fruit in fruits:
        copy_fruits.add(user_fruit)
        # return copy_fruits
    else:
        print('Fruit not found')
    return copy_fruits

print(check_set())