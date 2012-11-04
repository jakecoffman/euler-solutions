from itertools import combinations, ifilter

def is_abundant(num):
    s = 0   
    for i in xrange(1, num):
        if num%i == 0:
            s += i
            if s > num:
                return True
    return False

abund = set(ifilter(is_abundant, xrange(1, 28124/2)))
s = 0
for i in xrange(1, 28124):
    if not any((i-a in abund) for a in abund):
        s += i
        
print s