# Ha, I can't find a faster way at the moment

def pentagonal():
    i = 1
    while True:
        yield i*(3*i-1)/2
        i += 1
        
import math
        
ps = []
p = pentagonal()
founds = []
r = 2400
for x in xrange(r):
    if x == r/4:
        print "25%"
    elif x == r/2:
        print "50%"
    elif x == 3*r/4:
        print "75%"
    for y in xrange(x, r):
        l = len(ps)
        while x+1 > l or y+1 > l:
            ps.append(p.next())
            l = len(ps)
        if ps[x] + ps[y] in ps:
            print x+1, y+1
            if math.fabs(ps[x] - ps[y]) in ps:
                founds.append(math.fabs(ps[x] - ps[y]))
                break
print founds
print ps[3], ps[6]