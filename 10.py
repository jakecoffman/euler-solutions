from multiprocessing import Pool
import math

def is_prime(n):
    if n == 2:
        return 2
    if n%2 == 0:
        return 0
    if any(n%i == 0 for i in range(3, int(math.sqrt(n))+1, 2)):
        return 0
    return n
    
if __name__ == "__main__":
    p = Pool(7)
    
    it = p.imap(is_prime, xrange(2, 2000000), 1000)
    
    sum = 0
    try:
        while True:
            sum += it.next()
    except StopIteration:
        pass
    
    print sum
    