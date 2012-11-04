def fib(x=0, y=1):
    while True:
        yield x
        x, y = y, x+y
        
f = fib()
sum = 0
value = f.next()

while value < 4000000:
    if value%2 == 0:
        sum += value
    value = f.next()
    
print sum