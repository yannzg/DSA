# Implementation of Inorder Traversal 

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder_traversal(root):

    if root is None:
        return []
    
    result = []
    stack = []
    current = root

    while stack or current:

        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)

        current = current.right

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

#         a
#        / \
#       b   c
#      / \   \
#     d   e   f

print(inorder_traversal(a))