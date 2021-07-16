import stdio
import sys

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])
result = False

if(x < y < z or x > y > z):
    result = True

stdio.writeln(result)
