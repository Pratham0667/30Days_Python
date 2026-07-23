#Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

country_dict = [{'country': country.upper(), 'city': city.upper()}
               for [(country,city)] in countries]
print(country_dict)
