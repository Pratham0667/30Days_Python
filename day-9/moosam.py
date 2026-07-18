month = input("Enter the month: ").capitalize()

if month in ["September", "October", "November"]:
    print("Season: Autumn")
elif month in ["December", "January", "February"]:
    print("Season: Winter")
elif month in ["March", "April", "May"]:
    print("Season: Spring")
elif month in ["June", "July", "August"]:
    print("Season: Summer")
else:
    print("Invalid month! Please enter a valid month name.")