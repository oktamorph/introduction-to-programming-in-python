import math
import stdio
import sys

e = math.e
P = int(sys.argv[1]) # principal
r = int(sys.argv[2]) # rate
t = int(sys.argv[3]) # year
months = 12

result = P * e ** (r * t)
stdio.writeln(result)
stdio.writeln("Monthly payment: " + str(result / months))
