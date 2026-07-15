fruits  = ("apple" , "jackfruit" , "tomato")
vegi = ("califlower" , "potato" , "onion")
animal_products = ("egg" , "meat" , "fish")
print(f"FRUITS : {fruits}")
print(f"VEGI: {vegi}")
print(f"ANIMAL PRODUCTS : {animal_products}")


food_stuff_tp = fruits+ vegi + animal_products
print(f"FOOD STUFF TUPLE : {food_stuff_tp}")


food_stuff_li = list(food_stuff_tp)
print(f"FOOD STUFF LIST : {food_stuff_li}")


if len(food_stuff_li)%2 == 0 :
  middle = food_stuff_li[len(food_stuff_li)//2 -1 : len(food_stuff_li)//2+1]
else :
  middle = food_stuff_li[len(food_stuff_li)//2] 
print(f"THE MIDDLE ELEMENT : {middle}")


first_three = food_stuff_li[:3]
print(f"THE FIRST THREE ELEMENT : {first_three}")


last_three = food_stuff_li[-3:]
print(f"THE LAST THREE ELEMENT : {last_three}")

del food_stuff_tp
