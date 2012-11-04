
idf = ''
for i in xrange(1, 1000001):
    idf += str(i)
    
print int(idf[11])
    
print int(idf[0])*\
      int(idf[9])*\
      int(idf[99])*\
      int(idf[999])*\
      int(idf[9999])*\
      int(idf[99999])*\
      int(idf[999999])
