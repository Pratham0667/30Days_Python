#Declare a function called categorize_countries that returns a list of countries with some common pattern
import countries 

def categorize_countries(countries_list, pattern):
  return [country for country in countries_list if pattern.lower() in country.lower()]
  
land_countries = categorize_countries(all_countries, "land")  #end with "land"
print(land_countries)

ia_countries = categorize_countries(all_countries, "ia")
print(ia_countries)     #end with "ia"
