#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
#Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(celsius):
  fahren = (celsius * (9/5)) + 32
  return fahren

celsius = float(input("Enter the temperature in celsius: "))
fahrenheit = convert_celsius_to_fahrenheit(celsius)
print(f"Degree in fahrenheit after conversion {fahrenheit}")
