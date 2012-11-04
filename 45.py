def triangle(n=1):
    while True:
        yield n*(n+1)/2
        n += 1
        
def pentagonal(n=1):
    while True:
        yield n*(3*n-1)/2
        n += 1
        
def hexagonal(n=1):
    while True:
        yield n*(2*n-1)
        n += 1

t = triangle()
p = pentagonal()
h = hexagonal()

_t = t.next()
_p = p.next()
_h = h.next()

import time

tm = time.time()

founds = []
while True:
    if _t == _p == _h:
        founds.append((_t, _p, _h))
        if len(founds) == 3:
            break
        _t = t.next()
    else:
        # First see if one is clearly lower than the other two
        if _t < _p and _t < _h:
            _t = t.next()
        elif _p < _t and _p < _h:
            _p = p.next()
        elif _h < _p and _h < _t:
            _h = h.next()
        else:
            # Two of them are equal, increment the slower-growing one
            if _p == _h:
                _p = p.next()
            elif _t == _h:
                _t = t.next()
            elif _t == _p:
                _t = t.next()
            elif _t == _h:
                _t = t.next()
            # Something oopsed up here
            else:
                print "Oopsed at:", _t, _p, _h
                break
print founds

print time.time() - tm