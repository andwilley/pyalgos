from collections import deque

class Node:
    def __init__(self, value, left, right):
        self.left = left
        self.right = right
        self.value = value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

b = Node('B', None, None)
d = Node('D', None, None)
c = Node('C', d, None)
a = Node('A', c, None)
e = Node('E', a, b)
f = Node('F', None, None)
g = Node('G', e, f)

#
def in_order_mirror_traversal(node):
    if node.right:
        in_order_mirror_traversal(node.right)
    print(node.value)
    if node.left:
        in_order_mirror_traversal(node.left)

# find the max depth of the tree
def dfts(node):
    unvisited = deque([])
    unvisited.append(node)
    max_depth = 0
    max_depth = 0
    while unvisited:
        current_node = unvisited.pop()
        if current_node.right:
            down = True
            unvisited.append(current_node.right)
        if current_node.left:
            down = True
            unvisited.append(current_node.left)
        if down:
            max_depth += 1
        down = False
    return max_depth
