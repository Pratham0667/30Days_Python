#Use filter to filter out countries containing 'land'.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def land(country):
  if 'land' in country:
    return True
  return False

country_with_land = filter(land, countries)
print(list(country_with_land))

#Use filter to filter out countries having exactly six characters.
def character(country):
  if len(country) == 6:
    return True
  return False

country_with_six_characters = filter(character, countries)
print(list(country_with_six_characters))

#Use filter to filter out countries containing six letters and more in the country list.
def character(country):
  if len(country) >= 6:
    return True
  return False

country_with_six_characters = filter(character, countries)
print(list(country_with_six_characters))

#Use filter to filter out countries starting with an 'E'
def character(country):
  if country[0] == 'E':
    return True
  return False

country_with_starting_E = filter(character, countries)
print(list(country_with_starting_E))
