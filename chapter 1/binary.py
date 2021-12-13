import sys
import stdio

n = int(sys.argv[1])

# Compute v as the largest power of 2 <= n.
v = 1
while v <= n // 2:
    v *= 2
    
# Cast out powers of 2 in decreasing order.
while v > 0:
    if n < v:
        stdio.write(0)
    else:
        stdio.write(1)
        n -= v
    v //= 2
    
stdio.writeln()
