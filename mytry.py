class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


ans = []


def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None


def postOrderIterative(root):

    if root is None:
        return

    stack = []

    while(True):

        while (root):

            if root.right is not None:
                stack.append(root.right)
            stack.append(root)

            root = root.left

        root = stack.pop()

        if (root.right is not None and peek(stack) == root.right):
            stack.pop()  # Remove right child from stack
            stack.append(root)  # Push root back to stack
            root = root.right  # change root so that the
            # righ childis processed next

        # Else print root's data and set root as None
        else:
            ans.append(root.data)
            root = None

        if (len(stack) <= 0):
            break


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

postOrderIterative(root)
print(ans)
