for x in xrange(1, 10000000):
    multiplied = [6*x, 5*x, 4*x, 3*x, 2*x]
    strings = (sorted(list(str(result))) for result in multiplied)
    string = sorted(list(str(x)))
    if all((s == string for s in strings)):
        print x, multiplied
        break
    