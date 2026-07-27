#Calculate the time difference between now and new year.

from datetime import date, datetime
today = date(year=2026, month=7, day=26)
new_year = date(year=2027, month=1, day=1)
time = new_year - today
print(time)    #OUTPUT: 159 days, 0:00:00

#Calculate the time difference between 1 January 1970 and now.

given_date = date(year=1970, month=1, day=1)
today = date(year=2026, month=7, day=26)
time = today - given_date
print(time)    #OUTPUT: 20660 days, 0:00:00
