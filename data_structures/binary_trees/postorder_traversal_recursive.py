# Implementation of Postorder Traversal using recursion

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def postorder_traversal(root):

    if root is None:
        return []
    
    result = []

    result += postorder_traversal(root.left)
    result += postorder_traversal(root.right)
    result.append(root.val)


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

print(postorder_traversal(a))