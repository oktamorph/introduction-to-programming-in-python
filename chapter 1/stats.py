import sys
import stdio

n = int(sys.argv[1])
sum = 0
average = 0
minimum = 0
maximum = 0

for i in range(n + 1):
    sum += i
    
    if(i < minimum):
        minimum = i
    if(i > maximum):
        maximum = i    
        
average = sum / n    

stdio.writeln("Average value: " + str(average))
stdio.writeln("Minimum value: " + str(minimum))
stdio.writeln("Maximum value: " + str(maximum))
