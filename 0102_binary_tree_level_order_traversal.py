if not root:
     return[]

result= []
queue= deque([root])

while queue:
        level= []
        levelsize= len(queue)

        for _ in range(levelsize):
            node= queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)        

return result                