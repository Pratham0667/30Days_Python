first_name , last_name = input("eneter the first name :") , input("eneter the last name  :")

print(first_name , "\n");
print(len(first_name), "\n");


print(len(last_name), "\n");
print(len(last_name ), "\n");


len1 = len(first_name)
len2 = len(last_name)


if  len1 > len2 :
  print(first_name ,",first name  has greater number of char")
elif len2 > len1: 
  print(last_name ," ,last name has greater number of char")
else :
  print("both have same no of chars!")


