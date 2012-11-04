from math import factorial as f

i = 0
for n in xrange(23, 101):
    for r in xrange(1, n+1):
        if f(n)/(f(r)*f(n-r)) > 1000000:
            i += 1
            
print i