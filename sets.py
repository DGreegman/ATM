st = { 'itme1', 'itme2', 'itme3' }
# lst = ['itme1', 'itme2', 'itme3']
# tpl = ('itme1', 'itme2', 'itme3')

# fruits = {'apple', 'orange', 'banana', 'pinanapple'}
# print(len(fruits))
# print(fruits)
# Check if an item exists in the set
# name = 'Rose'
# lastname = 'okafor'
# print(f'{name} is a girl and her surname is ', lastname)
def check_item(item):
    
    return item
""" 
while True:

    item = input('Enter the name of the item you wan to check ')
    if item in fruits:
        print(check_item('rose'))
        break
    else:
        print(f"{item} is not in the set. Please try again.")
 """
# print(check_item('hello'))


def my_update(item=[]):
    names = set()
    names.update(item)
    return names

lst = ['hello', 'chief', 'chief']
print(my_update(lst))

set_list = {'itme1', 'itme2', 'itme3'}
set_list.remove('itme1')
print(set_list)
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)
del fruits
print(fruits)
""" def set_update():
    st = {'item1', 'item2', 'item3', 'item4'}
    st.update(['item5','item6','item7'])
    return st

print(set_update()) """