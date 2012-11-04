def palindrome(num):
    strnum = str(num)
    half = len(strnum)/2
    if strnum[:half] == ''.join(list(reversed(strnum[half:]))):
        return True
    return False
    
found = []
for i in xrange(999, 0, -1):
    for j in xrange(999, 0, -1):
        p = i*j
        if palindrome(p):
            found.append(p)

print sorted(found)[-1]