#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
import random

def list_of_rgb_colors(n):
  color_list = []
  color = 0
  for color in range(n):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb_colors = (f"rgb({r},{g},{b})")
    color_list.append(rgb_colors)
  return color_list 
  
n = int(input("Enter the number of colors needed: "))
print(list_of_rgb_colors(n))
