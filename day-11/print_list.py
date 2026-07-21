#Declare a function named print_list. 
#It takes a list as a parameter and it prints out each element of the list.

def print_list(*list):
  for i in list:
    print(i)

print_list('mango','apple','strawberry')
