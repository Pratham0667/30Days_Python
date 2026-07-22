#Write a function which generates a six digit/character random_user_id
import random 
import string

def random_user_id():
  characters = string.ascii_letters + string.digits
  random_id = ''.join(random.choice(characters) for i in range(6))
  return random_id

print(random_user_id())

#Modify the previous task. 
#Declare a function named user_id_gen_by_user. 
#It doesn’t take any parameters but it takes two inputs using input(). 
#One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
  num_of_char = int(input("Enter number of characters: "))
  num_of_id = int(input("Enter number of IDs to be generated: "))
  ids = 0
  while ids <= num_of_id:
    characters = string.ascii_letters + string.digits
    random_id = ''.join(random.choice(characters) for i in range(num_of_char))
    ids += 1
  return random_id

print(user_id_gen_by_user())
