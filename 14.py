from multiprocessing import Pool
import time

def sequence(n):
    while True:
        if n%2 == 0:
            n = n/2
            yield n
        else:
            n = 3*n+1
            yield n
            
def length(n):
    s = sequence(n)
    # Accounts for starting number and 1
    i = 2
    while s.next() > 1:
        i += 1
    return n, i

if __name__ == "__main__":
    p = Pool(7)
    
    it = p.imap(length, xrange(1000000), 100)
    lengths = []
    t = time.time()
    try:
        while True:
            lengths.append(it.next())
    except StopIteration:
        pass
    
    greatest = (0, 0)
    for n, l in lengths:
        if l > greatest[1]:
            greatest = n, l
            
    print greatest
    
    print time.time() - t