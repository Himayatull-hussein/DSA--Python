stack= []
greaternum= {}

for num in nums2:
            while stack and num> stack[-1]:
                smaller= stack.pop()
                greaternum[smaller]= num

            stack.append(num)


for num in stack:
        greaternum[num]= -1

return[greaternum[num] for num in nums1]    