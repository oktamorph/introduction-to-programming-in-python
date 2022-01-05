import sys
import stdio

n = int(sys.argv[1])
power = 0

if(n < 0):
    stdio.writeln("input number is negative")
else:
    while(2 ** power <= n):
        stdio.writeln(2 ** power)
        power += 1
        
