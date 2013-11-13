from primes import isprime

def poly(a,b,n):
    return n*n + a * n + b
    
def run_length(a,b):
    n = 0
    while True:
        #print n
        if isprime(poly(a,b,n)):
            n += 1
        else:
            return n
best = 0
ba = 0
bb = 0

max = 10000
print run_length(999,999)
#exit()
for a in xrange(-max,max):
    print str(a) + ": " + str(best)
    for b in xrange(-max,max):
        l = run_length(a,b)
        if l > best:
            best = l
            ba = a
            bb = b
  
print  
print ba
print bb
print best
print ba*bb