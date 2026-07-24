#Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
import countries

def get_last_ten_countries():
  return countries[-10:]

last_ten = get_last_ten_countries()
print(last_ten)  #OUTPUT: ['United Kingdom','United States','Uruguay','Uzbekistan','Vanuatu','Vatican City','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe']
