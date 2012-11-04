def series(n):
    return reduce(lambda x,y: x+y, (x**x for x in xrange(1, n+1)))
    
print str(series(1000))[-10:]