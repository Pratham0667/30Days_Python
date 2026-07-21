#Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return "Slope is undefined (vertical line)"

    slope = (y2 - y1) / (x2 - x1)
    return slope

result = calculate_slope(2, 3, 6, 11)
print(result)
