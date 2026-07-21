#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
  if month == "september" or month == "october" or month == "november":
    return("The season is Autumn")
  elif month == "december" or month == "january" or month == "february":
    return("The season is Winter")
  elif month == "march" or month == "april" or month == "may":
    return("The season is Spring")
  else:
    return("The season is Summer")

month = input("Enter the current month: ")
season = check_season(month)
print(f"Current season is {season}")
