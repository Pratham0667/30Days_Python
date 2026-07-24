#Use reduce to sum all the numbers in the numbers list.

numbers = ['1', '2', '3', '4', '5']  
def add(x, y):
    return int(x) + int(y)

total = reduce(add, numbers)
print(total)

#Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

joined_countries = reduce(lambda x, y: f"{x}, {y}", countries)
country_string = joined_countries.rsplit(", ", 1)
sentence = f"{country_string[0]}, and {country_string[1]} are north European countries"
print(sentence)

