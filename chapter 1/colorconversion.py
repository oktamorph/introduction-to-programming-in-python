import math
import stdio

import sys

red = float(sys.argv[1])
green = float(sys.argv[2])
blue = float(sys.argv[3])

cyan = 0.0
magenta = 0.0
yellow = 0.0
black = 0.0

if(red == 0.0 and green == 0.0 and blue == 0.0):
    black = 1.0
else:
    w = max(red / 255, green / 255, blue / 255)
    cyan = (w - (red / 255)) / w
    magenta = (w - (green / 255)) / w
    yellow = (w - (blue / 255)) / w
    black = 1 - w
    
stdio.writeln("Red: " + str(red) + "; " + "Green: " + str(green) + "; " + "Blue: " + str(blue) + "\n"
              "Cyan: " + str(cyan) + "; " + "Magenta: " + str(magenta) + "; " + "Yellow: " + str(yellow) + "; " + "Black: " + str(black))    
