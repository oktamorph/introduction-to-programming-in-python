import math
from sys import argv
import stdio

x1 = math.degrees(float(argv[1]))
y1 = math.degrees(float(argv[2]))

x2 = math.degrees(float(argv[3]))
y2 = math.degrees(float(argv[4]))

d = 60 * math.degrees(math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) +
                   math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * math.cos(math.radians(y1) - math.radians(y2))))

stdio.writeln("Distance is " + str(d) + " nautical miles")
