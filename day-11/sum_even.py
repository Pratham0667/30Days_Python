#Declare a function named sum_of_even. 
#It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(num):
    total = 0
    for i in range(num + 1):
        if i % 2 == 0:
            total += i
    return total

print(sum_of_even(10))
