def is_palindrome(n):
    s = str(n)
    l = len(s)
    if l%2 == 0:
        return s[:l/2] == ''.join(reversed(s[l/2:]))
    else:
        return s[:l/2] == ''.join(reversed(s[l/2+1:]))
        
def reverse(n):
    return int(''.join(reversed(str(n))))
    
lychrels = []
for i in xrange(1, 10000):
    n = i
    for j in xrange(50):
        t = n + reverse(n)
        if is_palindrome(t):
            break
        n = t
    else:
        lychrels.append(i)
    
print len(lychrels)