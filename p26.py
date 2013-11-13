def findtenk(d):
    k = 1
    while k < 1000:
        r = pow(10,k) - 1
        if r% d  == 0:
            return r
        k+=1
            
            
bestl = 0
d = 1

for i in xrange(1,1000):
    print i
    l = len(str(findtenk(i)))
    if l > bestl:
        bestl = l
        d = i
        
print bestl
print d
            