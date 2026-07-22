#Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
import random

def shuffle_list(list):
  shuffled = random.ample(list, len(list))
  return shuffled

my_list = [1,2,3,4,5,6,7,8,9]
print(shuffle_list(my_list))
