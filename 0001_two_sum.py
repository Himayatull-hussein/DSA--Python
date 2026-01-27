d={}
for i in range(0,len(nums)):
    value = nums[i]
    difference = target-value
    if value not in d:
        d[differnce]= i
    else:
        currentindex = i
        previousindex= d[value]
        return [currentindex, previousindex]    
