resset= set()
res= 0
l= 0
for i in range(0,len(s)):
        while s[i] in resset:
                resset.remove(s[l])
                l+=1
        resset.add(s[i])
        res= max(res, i- l+1)

return res                
