it_companies = ["Facebook", "Google" ,"Mircosoft" , "Apple" , "IBM" , "Oracle" , "Amazon"]
print(f"THE INITAL IT COMPANY LIST : \n {it_companies}")

print(f"THE length IT COMPANY LIST : {len(it_companies)}")

print(f" THE FIRST COMPANY :{it_companies[0] } \n THE MIDDLE COMPANY : { it_companies[len(it_companies)//2]}  THE LAST : {it_companies[-1]}")

it_companies[1] = "GOOGLE"
print(f" THE UPDATED IT COMPANY : \n  {it_companies}")


it_companies.append("META")
it_companies.insert(len(it_companies)//2 , "WHATS APP")
print(f" THE IT COMPANY AFTER ADDED TWO MORE COMPANY : \n {it_companies}")


it_companies[2] = it_companies[2].upper()
print(f" THE IT COMPANY UPDAATED COMPANY : \n {it_companies}")

joined =" # ".join(it_companies)

print(f" THE IT COMPANY UPDAATED COMPANY : \n {joined}")

isPresnt = "META" in it_companies
print(f" IS META PRESENT IN IT COMAPANY LIST : {isPresnt}")

it_companies.sort()
print(f" THE SORTED COMPANY : \n {it_companies}")

it_companies.reverse()
print(f" THE COMAPANY IN REV : \n {it_companies}")

print(f"Slice out the first 3 companies from the list  :  {it_companies[:3]}")

print(f" Slice out the last 3 companies from the list : {it_companies[-3:]}")

if len(it_companies) % 2 == 0:
    middle = it_companies[len(it_companies)//2 - 1 : len(it_companies)//2 + 1]
else:
    middle = it_companies[len(it_companies)//2]

print(f"THE MIDDLE ELEMET : {middle} ")



it_companies.pop(0)
it_companies.pop(len(it_companies)//2)
it_companies.pop(-1)
print(f" THE IT COMPANY UPDAATED COMPANY : \n {it_companies}")

it_companies.clear()
print(f" THE IT COMPANY UPDAATED COMPANY : \n {it_companies}")

del it_companies