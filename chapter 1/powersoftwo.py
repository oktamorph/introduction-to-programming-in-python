import sys
import stdio

n = int(sys.argv[1])
power = 1

for i in range(n + 1):
    stdio.writeln(str(i) + ' ' + str(power))
    power *= 2

