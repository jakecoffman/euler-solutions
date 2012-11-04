# This is why I love high level languages
from itertools import permutations

print list(permutations('012', 3))

p = list(permutations('0123456789'))

print ''.join(p[999999])