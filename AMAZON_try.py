class Node:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lca(root, n1, n2):
    if not root:
        return root

    if root.val in [n1, n2]:
        return root

    lh = lca(root.left, n1, n2)
    rh = lca(root.right, n1, n2)

    if lh and rh:
        return root

    if lh:
        return lh
    return rh


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print("LCA(4,5) = ", lca(root, 4, 5).val)
print("LCA(4,6) = ", lca(root, 4, 6).val)