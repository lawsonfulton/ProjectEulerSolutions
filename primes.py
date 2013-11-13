def loadprimes(n):
    if n > 10000:
        raise
        
    primes = n*[-1]
    
    f = open("10000primes.txt",'r')
    strings = f.read().split()
    
    for i in xrange(n):
        primes[i] = int(strings[i])
        
    return primes
    
def isprime(n):
    if n < 2:
        return False
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1
    return True