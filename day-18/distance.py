#Extract these numbers from this whole text and find the distance between the two furthest particles.

import re

text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

numbers = [int(n) for n in re.findall(r'-?\d+', text)]  #int(n) covert the list of strings (numbers are stored as string in list) to list of integer 
sorted_numbers = sorted(numbers)
distance = max(sorted_numbers) - min(sorted_numbers)

print(f"Extracted: {numbers}")
print(f"Sorted: {sorted_numbers}")
print(f"Distance: {distance}")
