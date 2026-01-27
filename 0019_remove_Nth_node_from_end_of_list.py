dummy= ListNode(0, head)
slow= dummy
fast= head

for i in range(n):
        fast= fast.next


while fast is not None:
        slow= slow.next
        fast= fast.next

slow.next= slow.next.next

return dummy.next    
