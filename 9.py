def is_pythag(a, b, c):
    return a*a + b*b == c*c

for i in xrange(3, 1000):
    for j in xrange(i, 1000):
        for k in xrange(j, 1000):
            if is_pythag(i, j, k) and i+j+k == 1000:
                print i*j*k
                exit()
                