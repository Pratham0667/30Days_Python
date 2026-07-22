#Write a function which returns an array of seven random numbers in a range of 0-9. 
#All the numbers must be unique.
import random

def random_array():
  return random.sample(range(0, 10), 7)

print(random_array())
