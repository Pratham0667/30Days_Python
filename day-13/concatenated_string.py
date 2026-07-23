#Change the following list to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

name_string = [(f"{fname} {lname}") for [(fname,lname)] in names]
print(name_string)
