class Node:

    # Constructor to create a new tree node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def findLCA(root, n1, n2):
    if not root:
        return None

    if root.key in [n1, n2]:
        return root

    lr = findLCA(root.left, n1, n2)
    rr = findLCA(root.right, n1, n2)

    if lr and rr:
        return root

    if lr is not None:
        return lr
    return rr


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print("LCA(4,5) = ", findLCA(root, 4, 5).key)
print("LCA(4,6) = ", findLCA(root, 4, 6).key)
print("LCA(3,4) = ", findLCA(root, 3, 4).key)
print("LCA(2,4) = ", findLCA(root, 2, 4).key)
