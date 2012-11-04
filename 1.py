def multiples_of(key, number):
    return number % key == 0
    
import functools
multiple_of_3 = functools.partial(multiples_of, 3)
multiple_of_5 = functools.partial(multiples_of, 5)

multiples = (i for i in xrange(1, 1000) if multiple_of_3(i) or multiple_of_5(i))

print sum(multiples)