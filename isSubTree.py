def isSubTree( mainTree, subTree):

	queue = deque([])
	if mainTree:
		queue.appendleft(mainTree)
	if not mainTree and not subTree:
		return True
	if mainTree and not subTree:
		return True

	while queue:
		current = queue.pop()
		if current.value == subTree.value:
			if compareTrees(current, subTree):
				return True
		if current.left:
			queue.appendleft(current.left)
		if current.right:
			queue.appendleft(current.right)
	return False

def compareTrees(mainTreeNode, subTreeNode):
	if not mainTreeNode and subTreeNode:
		return False
	if not mainTreeNode and not subTreeNode:
		return True
	if not subTreeNode:
		return True
	if mainTreeNode.value != subTreeNode.value:
		return False
	return compareTrees(mainTreeNode.left, subTreeNode.left) and compareTrees(mainTreeNode.right, subTreeNode.right)