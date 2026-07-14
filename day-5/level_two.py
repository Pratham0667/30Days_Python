
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list
ages.sort()
print(f"Sorted Ages: {ages}")

# Find the minimum and maximum age
min_age = ages[0]
max_age = ages[-1]

print(f"Minimum Age: {min_age}")
print(f"Maximum Age: {max_age}")

# Add the minimum and maximum age again
ages.append(min_age)
ages.append(max_age)

print(f"Ages after adding min and max: {ages}")

# Find the median
if len(ages) % 2 == 0:
    middle1 = ages[len(ages) // 2 - 1]
    middle2 = ages[len(ages) // 2]
    median = (middle1 + middle2) / 2
else:
    median = ages[len(ages) // 2]

print(f"Median Age: {median}")

# Find the average
total = sum(ages)
average = total / len(ages)

print(f"Average Age: {average}")

# Find the range
age_range = max_age - min_age

print(f"Age Range: {age_range}")

# Compare absolute differences
min_difference = abs(min_age - average)
max_difference = abs(max_age - average)

print(f"|Minimum - Average| = {min_difference}")
print(f"|Maximum - Average| = {max_difference}")