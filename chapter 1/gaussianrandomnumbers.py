import math
import stdrandom
import stdio
import sys

u = stdrandom.random.random()
v = stdrandom.random.random()
w = math.sin(2 * math.pi * v) * (-2 * math.log(u)) ** (1 / 2)

stdio.writeln(w)