#Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(items):
    return [item for item in items if isinstance(item, str)]

mixed_list = [1, "hello", 3.14, "world", True, "python"]
string_list = get_string_lists(mixed_list)
print(string_list)  # Output: ['hello', 'world', 'python']   
