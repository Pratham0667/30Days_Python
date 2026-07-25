print("--- TEST VALUES FOR y = x^2 + 6x + 9 ---")

# Prompts you to type in any number for x
x = float(input("ENTER A VALUE FOR X: "))

# The math equation
y = (x ** 2) + (6 * x) + 9

print(f"When x is {x}, y is equal to {y}")

if y == 0:
    print(" You found the zero point!")
else:
    print(" Try another number!")