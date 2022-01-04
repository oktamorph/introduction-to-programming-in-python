import stdio
import sys

argument = int(sys.argv[1])

if(argument >= 0 and argument < 1000):
    for i in range(argument):        
        if(i % 10 == 0 or i % 100 == 0):
            stdio.writeln(str(i + 1) + 'st Hello')
        elif(i % 10 == 1 or i % 100 == 1):
            stdio.writeln(str(i + 1) + 'nd Hello')            
        elif(i % 10 == 2 or i % 100 == 2):
            stdio.writeln(str(i + 1) + 'rd Hello')
        else:
            stdio.writeln(str(i + 1) + 'th Hello')
else:
    stdio.writeln("i is more than 1000")
