def yrange(start, end, step=1):
    n = start
    while n < end:
        yield n
        n += step

def is_prime(num):
    for x in yrange(2, num):
        if num%x != 0:
            return False
    return True
    
from itertools import permutations
digits = list('123456789')
shortlist = []
for x in xrange(9, 0, -1):
    for p in permutations(''.join(digits[:x]), x):
        if is_prime(int(''.join(p))):
            shortlist.append(int(''.join(p)))
print sorted(shortlist)