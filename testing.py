def same_data_type(lst):
    if not isinstance(lst, list):
        return 'empty'
    firt_item = type(lst[0])
    
    for item in lst: 
        if type(item) != firt_item:
            return False
    
    return True

print(same_data_type(2))  