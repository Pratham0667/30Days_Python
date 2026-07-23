#Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
non_positive = [i for i in numbers if i <= 0]
print(non_positive)
