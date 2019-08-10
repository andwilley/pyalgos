# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def btreeGameWinningMove(self, root, n, x):
    """
    :type root: TreeNode
    :type n: int
    :type x: int
    :rtype: bool
    """
    tracker = {
        'aboveRed': 0,
        'belowRed': 0,
        'aboveNull': 0,
        'belowNull': 0
    }

def recurs(self, node, tracker, belowRed, belowNullChildofRed, x):
    if not node.left and not node.right:
        return tracker
    if node.val == x:
        belowRed = True
    if (not node.left or not node.right) and belowRed:
        belowNullChildofRed = True
    if node.left:
        return recurs(node.left, tracker, belowRed, belowNullChildofRed)
    if node.right:
        return recurs(node.right, tracker, belowRed, belowNullChildofRed)

def btreeGameWinningMoveActual(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """

        subtree_count = {
            'parent': 0,
            'left': 0,
            'right': 0
        }

        subtree_count = self.recurs(root, subtree_count, True, False, False, x)
        # sum of any 2 is greater than the other...
        return subtree_count['parent'] + subtree_count['left'] < subtree_count['right']\
                or subtree_count['parent'] + subtree_count['right'] < subtree_count['left']\
                or subtree_count['left'] + subtree_count['right'] < subtree_count['parent']

def recurs(self, node, subtree_count, above_red, below_left, below_right, x):
    if node.val == x:
        above_red = False
    subtree_count['parent'] += 1 if above_red else 0
    subtree_count['left'] += 1 if below_left else 0
    subtree_count['right'] += 1 if below_right else 0

    if not node.left and not node.right:
        return subtree_count


    if node.left:
        subtree_count = self.recurs(node.left, subtree_count, above_red, True if node.val == x else below_left, below_right, x)
    if node.right:
        subtree_count = self.recurs(node.right, subtree_count, above_red, below_left, True if node.val == x else below_right, x)

    return subtree_count