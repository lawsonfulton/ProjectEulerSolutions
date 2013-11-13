size = 10000000
length=size*[-1]
length[1] = 1

def collatz(n):
    l = 1
    
    while n > 1:
        
        if n < size:
            if length[n] != -1:
                return length[n] + l
            
        if n % 2 == 0:
            n = n/2
            l += 1
        else:
            n = 3*n + 1
            l += 1
        #print n
    return l
    

best = 0
bestn = 0
for i in xrange(1000001):
    l = collatz(i)
    length[i] = l
    if i %10000 == 0:
        print i
    if l > best:
        best = l
        bestn = i
print best
print bestn