#Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
country_code = {'Finland': 'FIN', 'Sweden': 'SWE', 'Norway': 'NOR'}

country_list = [[country.upper(), country_code[country], city.upper()] for [(country,city)] in countries]
print(country_list)
