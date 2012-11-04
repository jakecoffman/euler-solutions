def triangle(n):
    return int(0.5*n*(n+1))
    
def abc_value(word):
    v = 0
    for c in word:
        v += ord(c) - ord('A') + 1
    return v
    
print abc_value('SKY') == triangle(10)
    
triangles = []
for i in xrange(26*10):
    triangles.append(triangle(i))
    
words = open('words.txt').read().replace('"', '').split(',')
counter = 0
print triangles
for word in words:
    if abc_value(word) in triangles:
        counter += 1
        
print counter