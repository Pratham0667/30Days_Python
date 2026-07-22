#Write a function named rgb_color_gen. 
#It will generate rgb colors (3 values ranging from 0 to 255 each).
import random

def rgb_color_gen():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  return (r,g,b)

print(f'rgb{rgb_color_gen()}')
