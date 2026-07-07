# Implementation of Postorder Traversal 

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def postorder_traversal(root):

    if root is None:
        return []
    
    stack = [root]
    result = []

    while stack:
        current = stack.pop()
        result.append(current.val)

        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return result[::-1]



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

#         a
#        / \
#       b   c
#      / \   \
#     d   e   f

print(postorder_traversal(a))