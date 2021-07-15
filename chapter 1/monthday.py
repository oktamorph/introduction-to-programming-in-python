import stdio
import sys

month = int(sys.argv[1])
day = int(sys.argv[2])

result = False
if(month >= 3 and day >= 20 and day <= 31) and (month <= 6 and day >= 20 and day <= 30):
    result = True

stdio.writeln(result)
