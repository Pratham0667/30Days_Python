#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
#Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*nums):
  sums = 0
  for i in nums:
    if type(i) != int and type(i) != float:
      return(f"{i} is not a number type")
    else:
      sums += i
  return sums

result = add_all_nums(1,2,3,4,5,6,7,8,8,9)
print(result)
