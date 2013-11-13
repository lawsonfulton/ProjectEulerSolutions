
F = 1
FD = 1
n = 2

c = 1
while len(str(FD)) < 1000:
    n+=1 
    t = FD
    FD += F
    F = t
    if len(str(FD)) == c:
        print n
        c += 1
    
    
print n