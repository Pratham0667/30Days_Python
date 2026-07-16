it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print(f"THE LENGTH OF IT COMPANY SET : {len(it_companies)}")

it_companies.add("Twitter")
print(f"THE UPDATED IT COMPANY : {it_companies}")

multiple  = {"X" , "SUNNEXT" }
it_companies.update(multiple)
print(f"THE UPDATED IT_COMPANY : {it_companies}")

it_companies.remove("Apple")

print(f"THE UPDATED IT_COMPANY : {it_companies}")

# What is the difference between remove and discard
# remove raises error if item is not present discard doesnot rasit if its not there
