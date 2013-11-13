nums =[]
for a in xrange(2,101):
    for b in xrange(2,101):
        nums.append(a**b)

c = 0
while len(nums) != 0:        
    #print c l =
    x = nums[0]
    c += 1
    nums = filter (lambda a: a != x, nums)
    
print c