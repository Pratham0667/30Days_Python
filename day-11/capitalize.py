#Declare a function named capitalize_list_items. 
#It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(lst):
    capitalized_list = []
    for item in lst:
        capitalized_list.append(item.capitalize())
    return capitalized_list

print(capitalize_list_items(['apple', 'banana', 'mango']))
