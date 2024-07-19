def same_data_type(lst):
    if not isinstance(lst, list):
        return 'This is not a list'
    firt_item = type(lst[0])
    if len(lst) == 1:
        return 'You only have one item in the list, Nothing to compare'
    for item in lst: 
        if type(item) != firt_item:
            return False
    
    return True

print(same_data_type(5))  