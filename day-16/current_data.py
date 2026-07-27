#Get the current day, month, year, hour, minute and timestamp from datetime module

form datetime import datetime

current_date = datetime.now()
print(current_date)    #OUTPUT: 2026-07-26 13:31:20.153462

current_timestamp = current_date.timestamp()
print(current_timestamp)   #OUTPUT: 1785052880.153462

#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

date = current_date.timestamp("%m/%d/%Y, %H:%M:%S")
print(date)    #OUTPUT: 07/26/2026, 13:31:20
