# Implementation of Breadth-First Search Algorithm

from collections import deque

class Node(): 

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



def breadth_first_values(root):

    if root is None:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        result.append(current.val)

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)


    return result


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(breadth_first_values(a))