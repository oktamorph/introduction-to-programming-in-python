import math
import sys
import stdio

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

discriminant = b*b - 4.0*a*c
if(discriminant >= 0):
    d = math.sqrt(discriminant)
    if(a != 0):
        stdio.writeln((-b + d) / 2.0*a)
        stdio.writeln((-b - d) / 2.0*a)
    else:
        stdio.writeln("a is zero")
else:
    stdio.writeln("discriminant is negative")
