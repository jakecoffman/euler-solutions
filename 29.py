start, stop = 2, 100
seq = set()
for a in xrange(start, stop+1):
    for b in xrange(start, stop+1):
        seq.add(a**b)

print len(seq)