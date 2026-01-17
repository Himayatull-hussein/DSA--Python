m= nums[0]
c= 0
for i in nums:
    if c<0:
        c= 0
    c+=i    
    if c>m:
        m=c    