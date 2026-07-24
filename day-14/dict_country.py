#Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
import countries

def count_countries_by_letter(countries_list):
    counts = {}
    for country in countries_list:
        if country: 
            first_letter = country[0].upper() 
            if first_letter in counts:
                counts[first_letter] += 1
            else:
                counts[first_letter] = 1
    return counts

result = count_countries_by_letter(countries)
print(result) # Output: {'E': 1, 'F': 2, 'S': 2, 'D': 1, 'N': 1, 'I': 1, 'G': 1, 'B': 1, 'T': 1}   
