import sys
import stdio

first = int(sys.argv[1])
second = int(sys.argv[2])
third = int(sys.argv[3])

if(first == second and first == third):
    stdio.writeln("equal")
else:
    stdio.writeln("not equal")
    