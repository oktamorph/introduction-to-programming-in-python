import math
import stdio

import sys

inputLambda = float(sys.argv[1])
inputLambdaZero = float(sys.argv[2])
inputPhi = float(sys.argv[3])

x = str(inputLambda - inputLambdaZero)
y = str((1 / 2) * math.log((1 + math.sin(inputPhi) / (1 - math.sin(inputPhi)))))

stdio.writeln("X: " + x + "\n" + "Y: " + y)
