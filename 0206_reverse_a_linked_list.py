prev= None
cur= head
while cur!= None:
        temp= cur.next
        cur.next= prev
        prev= cur
        cur= temp
return prev    
