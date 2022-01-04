import sys
import stdio

first = float(sys.argv[1])
second = float(sys.argv[2])

if((first > 0.0 and second > 0.0) and (first < 1.0 and second < 1.0)):
    stdio.writeln(True)
else:
    stdio.writeln(False)
