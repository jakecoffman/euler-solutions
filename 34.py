import math
found = []
for i in xrange(3, 100000):
    string = str(i)
    if sum(math.factorial(int(c)) for c in string) == i:
        print i        
        found.append(i)
        
print sum(found)