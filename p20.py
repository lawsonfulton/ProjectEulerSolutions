
def fact(n):
    if n == 1:
        return 1
    
    return n * fact(n-1)
    
print sum([int(i) for i in list(str(fact(100)))])