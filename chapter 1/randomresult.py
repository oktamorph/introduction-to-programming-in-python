from random import random, seed
import sys
import stdio
import stdrandom

a = int(sys.argv[1])
b = int(sys.argv[2])
result = stdrandom.random.randint(a, b)

stdio.writeln(result)