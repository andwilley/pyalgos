class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.bts(root, 0, 0, *[])

    def bts(self, node, depth, acc, *depths):
        isEven = node.val % 2 == 0
        if isEven:
            depths += (depth + 2,)

        if depths and depth == depths[0]:
            acc += node.val
            depths = depths[1:]
        if node.left:
            acc = self.bts(node.left, depth + 1, acc, *depths)
        if node.right:
            acc = self.bts(node.right, depth + 1, acc, *depths)


        return acc