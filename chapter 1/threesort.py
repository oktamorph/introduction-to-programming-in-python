import math
from sys import argv
import stdio

x1 = int(argv[1])
x2 = int(argv[2])
x3 = int(argv[3])

smallest = min(x1, x2, x3)
biggest = max(x1, x2, x3)
middle = 0

if(x1 != smallest and x1 != biggest):
    middle = x1
elif(x2 != smallest and x2 != biggest):
    middle = x2
else:
    middle = x3

stdio.writeln("Smallest: " + str(smallest) + "\n" +
              "Middle: " + str(middle) + "\n" + 
              "Biggest: " + str(biggest)
              )
