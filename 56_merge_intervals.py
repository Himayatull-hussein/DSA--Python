intervals.sort()
a=[]
for start,end in intervals:
    if a and start <= a[-1][1]:
        a[-1][1]= max(a[-1][1],end)
    else:
        a.append([start, end])
return a            
