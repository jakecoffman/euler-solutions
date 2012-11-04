found = []
for i in xrange(2, 1000000):
    string = str(i)
    if sum((int(c)**5 for c in string)) == i:
        found.append(i)
        
print sum(found)