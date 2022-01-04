import math
import stdio
import sys

t = float(sys.argv[1]) # temperature
v = float(sys.argv[2]) # speed
if(math.fabs(t) <= 50):
    if(v >= 3):
        if(v <= 120):
            result = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * v ** 0.16
            stdio.writeln(result)
        else:
            stdio.writeln("t is bigger than 120")
    else:
        stdio.writeln("v is less than 3")
else:
    stdio.writeln("t is bigger than 50")

