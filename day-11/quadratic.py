#Quadratic equation is calculated as follows: ax² + bx + c = 0. 
#Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

import math

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2

    elif discriminant == 0:
        x = -b / (2 * a)
        return x

    else:
        return "No real solutions"
      
print(solve_quadratic_eqn(1, -5, 6))
