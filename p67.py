size = 100

tri = size*[size*[-1]]

def max_tot(r,c):
    if r == size - 1:
        return tri[r][c]
        
    return max(max_tot(r + 1,c) + tri[r][c], max_tot(r + 1, c + 1) + tri[r][c])

    

f = open("p67.in",'r')

for i in xrange(size):
    tri[i] = [int(j) for j in f.readline().split()]
    
print tri
print max_tot(0,0)