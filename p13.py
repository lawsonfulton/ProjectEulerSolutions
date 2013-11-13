
f = open("p13.in",'r')

numbers = [int(n) for n in f.read().split()]

print sum(numbers)