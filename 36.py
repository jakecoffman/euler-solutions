def is_palindrome(n):
    s = str(n)
    l = len(s)
    if l%2!=0:
        return s[:l/2] == ''.join(reversed(s[l/2+1:]))
    else:
        return s[:l/2] == ''.join(reversed(s[l/2:]))
    
    
pals = []
for i in xrange(1, 1000000):
    if is_palindrome(i) and is_palindrome(bin(i)[2:]):
        print i
        pals.append(i)
        
print sum(pals)