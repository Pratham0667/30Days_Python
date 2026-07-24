#Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.

import countries

def get_first_ten_countries():
    return countries[:10]

first_ten = get_first_ten_countries()
print(first_ten) #Output: ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria']   
