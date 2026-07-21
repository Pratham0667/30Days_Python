#Declare a function named sum_of_numbers. 
#It takes a number parameter and it adds all the numbers in that range.
#print(sum_of_numbers(5))  # 15
#print(sum_of_numbers(10)) # 55
#print(sum_of_numbers(100)) # 5050

def sum_of_numbers(num):
    total = 0

    for i in range(num + 1):
        total += i

    return total

print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))
