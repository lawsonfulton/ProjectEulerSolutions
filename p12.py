import time
def print_divisors(x):
    count = 2 #Start at 2 for 1 and x
    print str(x) + ":  " + str(1) + ",",
    for i in xrange(2,x / 2 + 1):
        if x % i == 0:
            count += 1
            print str(i) + ",",
    
    print str(x)
    return count

def count_divisors(x, best_run):
    count = best_run + 1 #Start at 2 for 1 and x
    
    for i in xrange(best_run, 1, -1):
        if x % i != 0:
            return (0,0)
            
    run = best_run
    for i in xrange(best_run + 1,x / 2 + 1):
        if x % i == 0:
            if run + 1 ==  i:
                run += 1
            elif run < best_run:
                return (count, run)
            count += 1
    return (count, run)

def count_divisors2(x, best_run):
    count = best_run + 1 #Start at 2 for 1 and x
    
    for i in xrange(best_run, 1, -1):
        if x % i != 0:
            return 0
            
    run = best_run
    for i in xrange(best_run + 1,x / 2 + 1):
        if x % i == 0:
            if run + 1 ==  i:
                run += 1
            elif run < best_run:
                return (count, run)
            count += 1
    return (count, run)
    
if __name__ == "__main__":
    c = print_divisors(1373692320)
    print c
    exit()
    T = 1
    n = 1
    divisors = 1
    best = 0
    best_run = 1
    new_run = 0
    while divisors < 500:
        divisors, new_run = count_divisors(T, best_run)
        
        if new_run >= best_run:
            best_run = new_run

        
        
            new_best = max(divisors,best)
            if new_best > best:
                best = new_best
                print str(n) + ", " + str(T) + ", " + str(divisors) +", " + str(best_run)
                #print_divisors(T)
            
        
        n += 1
        T += n
        #i = (n * (n + 1))/2
    
    
