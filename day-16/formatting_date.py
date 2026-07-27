#Today is 5 December, 2019. Change this time string to time.

from datetime import datetime
date_string = "5 December, 2019"
date = datetime.strptime(date_string, "%d %B, %Y")
print(date)    #OUTPUT: 2019-12-05 00:00:00
