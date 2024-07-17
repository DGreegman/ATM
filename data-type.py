# write a function to check if all the items in a list is of same data type

def check_data_type():
    lst = [1.4, 2.3]

    for mylist in lst:
        if type(mylist) == str or type(mylist) == float or type(mylist) == bool or type(mylist) == int: 
            return 'List contains mixed data types'
        else: 
            return type(mylist)
    # if type(lst[0]) == type(lst[1]):
    #     print('they are of same data type')
    # else:
    #     print('they are not of same data type')
    

print(check_data_type())

