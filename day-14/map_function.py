#Use map to create a new list by changing each country to uppercase in the countries list
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def upper_case(country):
  return country.upper()

country_uppercase = map(upper_case, countries)
print(list(country_uppercase))

#Use map to create a new list by changing each number to its square in the numbers list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def square(numbers):
  return numbers**2

squared_numbers = map(square,numbers)
print(list(squared_numbers))

#Use map to change each name to uppercase in the names list
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

def upper_case(names):
  return names.upper()

name_uppercase = map(upper_case, names)
print(list(name_uppercase))
