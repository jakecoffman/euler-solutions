def sum_squares(num):
    return sum(i*i for i in xrange(num+1))
    
def square_sum(num):
    return sum(xrange(num+1))**2
    
print square_sum(100) - sum_squares(100)