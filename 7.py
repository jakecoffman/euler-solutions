from multiprocessing import Pool
import math

def is_prime(n):
    for i in xrange(2,n):
        if n%i == 0:
            return 0
    return n
    
if __name__ == "__main__":
    p = Pool(7)
    
    it = p.imap(is_prime, xrange(3, 1000000, 2))
    
    i = 2
    while i < 10001:
        val = it.next()
        if val != 0:
            i += 1
    
    print val
    