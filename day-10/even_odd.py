#Use for loop to iterate from 0 to 100 and print only even numbers
print("EVEN NUMBERS: ")
for i in range(0,100,2):
  print(i)

#OR

print("EVEN NUMBERS: ")
for i in range(100):
  if i % 2 == 0:
    print(i)
    
#Use for loop to iterate from 0 to 100 and print only odd numbers
print("ODD NUMBERS: ")
for i in range(1,100,2):
  print(i)

#OR

print("ODD NUMBERS: ")
for i in range(100):
  if i % 2 != 0:
    print(i)
