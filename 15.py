
def make_map(size_squared):
    size_squared += 2
    map_string = []
    map_string.append(list('0'*(size_squared+1)))
    for i in xrange(size_squared-1):
        map_string.append(list('0' + '.'*(size_squared-1) + '0'))
    map_string.append(list('0'*(size_squared+1)))
    map_string[1][1] = 's'
    map_string[-2][-2] = 'f'
    return map_string

map = None
    
def d(x, y):
    return x, y+1
    
def r(x, y):
    return x+1, y
    
counter = 0
    
def follow_route(x, y):
    global counter
    done = False
    for move in xrange(2):
        a, b = directions[move](x, y)
        if map[a][b] != '0':
            if map[a][b] != 'f':
                follow_route(a, b)
            else:
                counter += 1
    
if __name__ == "__main__":
    global map
    directions = [d, r]
    x, y = (0, 0)
    x, y = x+1, y+1
    for i in xrange(1, 10):
        map = make_map(i)
        follow_route(x, y)
        print i, counter