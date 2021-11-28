import math
import stdio

import sys

# monthInput = int(sys.argv[1])
# dayInput = int(sys.argv[2])
# yearInput = int(sys.argv[3])
result = ""

monthInput = 2
dayInput = 14
yearInput = 2000

month = int(monthInput + 12 * ((14 - monthInput) / 12) - 2)
year = int(yearInput - (14 - month) / 12)
x = int(year + year / 4 - year / 100 + year / 400)
day = int((dayInput + x + (31 * month) / 12) % 7)

if(day == 0):
    result = "Sunday"
elif(day == 1):
    result = "Monday"
elif(day == 2):
    result = "Tuesday"
elif (day == 3):
    result = "Wednesday"
elif (day == 4):
    result = "Thursday"
elif (day == 5):
    result = "Friday"
elif(day == 6):
    result = "Saturday"
else:
    result = "An error in the calculations"    

stdio.writeln("Day of the week: " + result)
