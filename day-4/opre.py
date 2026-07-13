
str1 = "Coding "
str2 = "for "
str3 = "all"
company = str1 + str2 + str3
print(company)

print(f" THE LENGTH OF THE CONCATAED STRING  : {len(company)}")

print(f"ALL TO UPPER CASE : {company.upper()}") 
print(f"ALL TO A LOWER CASE  : {company.lower()}")


print(f"THE CAPTIALIZED VERSION : {company.capitalize()}")
print(f"THE TITLE VERSION : {company.title()}") # makes like a title
print(f"THE SWAPCASE VERSION : {company.swapcase()}") #makes captial to lower and lower to upper




company = "Coding For All"
first_word = company[:6]
print(first_word)


sub_company = "Coding " 
print(f" SERACH 1:{company.index(sub_company)}") #case senstive AF  | thorws error
print(f" SEARCH 2:{company.rindex(sub_company)}") #case senstive AF  | thorws error
print(f" SEARCH 3:{company.find(sub_company)}") #retuns -1 if not present | case senstive AF

replaced = company.replace("Coding", "python ") #doest repalce if not found
print(f" THE REPLACED CODING FOR ALL : {replaced}")



string = "python for everyone"
print(f" THE UN REPLACED :{string}")
stringRep = string.replace("for everyone" , "for all")
print(f" THE REPLACED  : {stringRep}")

spilting = company.split(" ")
print(spilting)

print(f" THE FIRST CHAR :{company[0]}")
print(f"THE LAST CHAR : {company[-1]}")
print(f"THE CHAR IN INDEX 10 : {company[9]}") # 10 is space so 


words1 = string.split(" ")
acronym1 = (words1[0][0] + words1[1][0] +words1 [2][0]).upper()
print(f"ACRONYM1 : {acronym1}")

words2 = company.split(" ")
acronym2 = (words2[0][0] + words2[1][0] + words2[2][0]).upper()
print(f"ACRONYM 2 : {acronym2}");

checking1 = company.index("C")
print(f" CHECKING OF C :{checking1}")

checking2 = company.index("f")
print(f" CHECKING OF C :{checking2}")

text = "Coding For All People"
checking3 = text.rfind("l")
print(f"lAST OCC : {checking3}")

answer1 = company.startswith("Coding ")
print(f"DOES CODING FOR ALL STARTS WITH CODING : {answer1}")

answer2 = company.endswith("Coding ")
print(f"DOES CODING FOR ALL ENDS WITH CODING :{answer2}")

text1 = "   Coding For All      "
print(f"INTIAL TXT : {text1}")
answer3 = text1.strip()
print(f"FINAL TEXT : {answer3}")
