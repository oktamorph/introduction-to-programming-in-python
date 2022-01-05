import sys
import stdio

n = int(sys.argv[1])

for i in range(1, n + 1):
    # Write the ith line.
    for j in range(1, n + 1):
        # Write the jth entry in the ith line.
        if (i % j == 0) or (j % i == 0):
            stdio.write('* ')
        else:
            stdio.write(' ')
    stdio.writeln(i)
stdio.writeln()

i = 1
j = 1
while i < n + 1:
    # Write the ith line.
    while j < n + 1:
        # Write the jth entry in the ith line.
        if (i % j == 0) or (j % i == 0):
            stdio.write('* ')
        else:
            stdio.write(' ')
        j += 1
    stdio.writeln(i)
    j = 1
    i += 1