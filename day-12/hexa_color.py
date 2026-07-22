#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. 
#Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. 
#Check the task 6 for output examples).
import random

def list_of_hexa_colors(n):
  characters = "0123456789ABCDEF"
  color_list = []
  nbr = 0
  for nbr in range(n):
    hexa_colors = '#' + ''.join(random.choice(characters) for i in range(6))
    color_list.append(hexa_colors)
  return color_list 
  
n = int(input("Enter the number of colors needed: "))
print(list_of_hexa_colors(n))
