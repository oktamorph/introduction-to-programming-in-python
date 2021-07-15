import math
import stdio
import sys

first = int(sys.argv[1])
second = int(sys.argv[2])

isEven = first % second == 0 or second % first == 0
stdio.writeln(isEven)
