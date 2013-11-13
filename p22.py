
f = open('p22.in','r')
names = [ n.strip('"') for n in f.read().split(",")]

names.sort()

total = 0

for i in xrange(len(names)):
    sum = 0
    name = list(names[i])
    for c in name:
        sum += ord(c) - 64
    
    total += (i+1) * sum
    
print total