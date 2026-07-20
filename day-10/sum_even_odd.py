#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
even_sum = 0
odd_sum = 0
for i in range(101):
  if i % 2 == 0:
    even_sum += i
  else: 
    odd_sum += i
print(f"The sum of all evens is {even_sum}. Add the sum of all odds is {odd_sum}")
