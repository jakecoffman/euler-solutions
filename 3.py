import math

def get_largest_prime_factor(n):
    i = int(round(math.sqrt(n)))
    while i > 1:
        if n%i == 0 and get_largest_prime_factor(i) == 0:
            return i
        i -= 1
    return 0
    
#factors = get_factors(600851475143)
print get_largest_prime_factor(600851475143)