empty_tuple = ();

brothers = ("anvith" , "ayush", "Diwatha" ) 
sisters = ("annapurna" , "aarna" ,"akshara")
print(f"BROTHER : {brothers} \n SISTERS = {sisters}");


siblings = brothers+sisters
print(f"SIBLINGS : {siblings}")


print(f"LENGTH : {len(siblings)}");


family_members = siblings+ ("mother" , "father")
print(f" THE FAMILY MEMBERS :{family_members}");


family_members = list(family_members)
*sibling , parent1, parent2 = family_members

print(f" THE SIBLINGS : {sibling} \n THE PARENTS : { parent1 ,parent2}")



