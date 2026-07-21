#Declare a function named sum_of_odds. 
#It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(num):
    total = 0
    for i in range(num + 1):
        if i % 2 != 0:
            total += i
    return total

print(sum_of_odds(10))
