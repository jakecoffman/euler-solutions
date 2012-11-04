def is_divisible(number):
    for i in xrange(21, 2, -1):
        if number%i != 0:
            return False
    return True
    
i = 20
while True:
    if is_divisible(i):
        print i
        break
    i += 20
    