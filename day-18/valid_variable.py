#Write a pattern which identifies if a string is a valid python variable
import re

def is_valid_variable(variable_name):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, variable_name))

print(is_valid_variable('first_name'))   
print(is_valid_variable('first-name'))   
print(is_valid_variable('1first_name'))  
print(is_valid_variable('firstname'))    
