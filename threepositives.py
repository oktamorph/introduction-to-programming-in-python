import math
import stdio
import sys

first = int(sys.argv[1])
second = int(sys.argv[2])
third = int(sys.argv[3])

result = True
if ((first >= second + third) or (second >= first + third) or (third >= first + second)):
    result = False

stdio.writeln(result)
