
abund = []

size = (28123*2)
can_sum =  size * [False]

def d(x):
    sum = 1
    for i in xrange(2,x / 2 + 1):
        if x % i == 0:
            sum += i

    return sum
    
def isabund(x):
    return d(x) > x

if __name__=="__main__":
    for i in xrange(28123):
        flag = isabund(i)
        if flag:
            abund.append(i)
            
        print str(i) + ": " + str(flag)
    print len(abund)

    n = len(abund)
    for a in xrange(1,n):
        for b in xrange(a,n):
            can_sum[abund[a]+abund[b]] = True
            
    print "doing sum"

    sum = 0
    for i in xrange(28123+1):
        if not can_sum[i]:
            print str(i) + ",",
            sum += i
            
    print sum