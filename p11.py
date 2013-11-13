
if __name__ == "__main__":
    g = [[0 for i in range(20)] for i in range(20)]
    
    f = open("p11.in",'r')
    numbers = [int(n) for n in f.read().split()]
    for i in xrange(20):
        for j in xrange(20):
            g[i][j] = numbers[j + i * 20]
            
    sums = []
    for r in xrange(3,16):
        for c in xrange(3,16):
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    if not (i == 0 and j == 0):
                        sum = 1
                        for k in xrange(4):
                            sum *= g[r + i * k][c + j * k]
                        
                        sums.append(sum)
    
    print max(sums)
    
