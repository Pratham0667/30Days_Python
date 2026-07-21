#Area of a circle is calculated as follows: area = π x r x r. 
#Write a function that calculates area_of_circle.
import math

def area_of_circle(r):
  area = math.pi * r * r
  return area 

r = float(input('Enter the radius of the circle: '))
circle = float(area_of_circle(r))
print(f"Area of the circle is {circle.2f}")
