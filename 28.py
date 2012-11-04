current = 0
step = 2

s = 0
limit = 1001 ** 2

spiral = range(1, limit + 1)

while current < limit:
    for i in xrange(4):
        if current > limit:
            break
        s += spiral[current]
        current += step
    step += 2

print s