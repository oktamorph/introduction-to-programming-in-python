import math
import stdio
import sys

G = 9.80665

x0 = float(sys.argv[1])
v0 = float(sys.argv[2])
t = float(sys.argv[3])

result = x0 + v0 * t - (G * t ** 2) / 2
stdio.writeln(result)
