def proper_divisors(num):
    for i in xrange(num-1, 0, -1):
        if num%i == 0:
            yield i
            
aimicable = set()
for b in xrange(1, 10001):
    a = sum(proper_divisors(b))
    if b == sum(proper_divisors(a)) and a != b:
        aimicable.add(a)
        aimicable.add(b)
print aimicable
print sum(aimicable)