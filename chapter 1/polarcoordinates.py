import math
import stdio
import sys

x = float(sys.argv[1])
y = float(sys.argv[2])
result = math.atan2(y, x)

stdio.writeln(result)
