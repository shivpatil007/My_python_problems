
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inOrder(root):
    def maxDepth(node):
        if node is None:
            return 0

        else:

            # Compute the depth of each subtree
            lDepth = maxDepth(node.left)
            rDepth = maxDepth(node.right)

            # Use the larger one
            if (lDepth > rDepth):
                return lDepth+1
            else:
                return rDepth+1

    b = maxDepth(root)

    a = [root]
    while len(a) < b**2:

        curr = a.pop(0)
        print(curr.data, end=" ")
        if curr.left is not None:
            a.append(curr.left)
        else:
            a.append(Node("null"))
        if curr.right is not None:
            a.append(curr.right)
        else:
            a.append(Node("null"))

    print()


""" Constructed binary tree is
			1
		/ \
		2	 3
	/ \
	4 5 """

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(7)
root.right.left = Node(100)

inOrder(root)
