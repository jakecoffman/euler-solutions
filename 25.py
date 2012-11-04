def fibby():
    i = 1
    j = 1
    yield i
    yield j
    while True:
        i, j = j, i+j
        yield j
        
f = fibby()
        
for i in xrange(1, 10000000):
    term = f.next()
    if len(str(term)) > 999:
        print i, term
        break
        