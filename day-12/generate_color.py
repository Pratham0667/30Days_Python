#Write a function generate_colors which can generate any number of hexa or rgb colors.
#   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
#   generate_colors('hexa', 1) # ['#b334ef']
#   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
#   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
import random

def generate_colors(color_type, n):
  colors = []
  
  if color_type == 'hexa':
      characters = "0123456789ABCDEF"
      nbr = 0
      for nbr in range(n):
        hexa_colors = '#' + ''.join(random.choice(characters) for i in range(6))
        colors.append(hexa_colors)
      return colors
    
  elif color_type == 'rgb':
    color = 0
    for color in range(n):
      r = random.randint(0,255)
      g = random.randint(0,255)
      b = random.randint(0,255)
      rgb_colors = (f"rgb({r},{g},{b})")
      colors.append(rgb_colors)
    return colors

  else:
    print("Invalid color type")

color_type = input("Enter the color type (hexa/rgb): ")
n = int(input("Enter the number of colors needed: "))
print(generate_colors(color_type, n))
