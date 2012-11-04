from multiprocessing import Pool
import time

def triangles():
    i = 0
    j = 1
    while True:
        i += j
        j += 1
        yield i

tris = triangles()

limit = 500

def factors(num):
    facts = []
    divisor = 1
    while (divisor <= int(num**0.5)):
        if num%divisor == 0:
            facts.append(divisor)
            facts.append(num/divisor)
        divisor += 1
    return facts, num
    
if __name__ == "__main__":
    p = Pool(7)
    
    it = p.imap(factors, tris, 10)
    
    t = time.time()
    try:
        while True:
            facts, num = it.next()
            amt = len(facts)
            if amt > limit:
                print num, amt
                break
    except StopIteration:
        pass

    print time.time() - t