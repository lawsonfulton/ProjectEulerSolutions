
mem = 10001 *[-1]

def d(x):
    #if mem[x] != -1:
    #    return mem[x]
        
    sum = 1
    for i in xrange(2,x / 2 + 1):
        if x % i == 0:
            sum += i
    
    mem[x] = sum
    return sum
    
def are_amic(a,b):
    if d(a) == b and d(b) == a:
            return True
    else: return False
    
sum = 0
for a in xrange(1,10001):
    for b in xrange(a,10001):
        if a != b:
            if are_amic(a,b):
                sum += a
                print str(a)+", " + str(b)
            
            
print sum