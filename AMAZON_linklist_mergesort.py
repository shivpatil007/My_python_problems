class Node:

    def __init__(self, data) -> None:
        self.val = data
        self.next = None


def myfun(head):
    if not head or not head.next:
        return head

    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    start = slow.next
    slow.next = None
    l, r = myfun(head), myfun(start)
    return myfun2(l, r)


def myfun2(l, r):
    if not l or not r:
        return l or r
    dummy = p = Node(0)
    while l and r:
        if l.val < r.val:
            p.next = l
            l = l.next
        else:
            p.next = r
            r = r.next
        p = p.next
    p.next = l or r
    return dummy.next


def print_LL(head):
    while head:
        print(head.val, end=" ")
        head = head.next


head = Node(3)
head.next = Node(6)
head.next.next = Node(9)
head.next.next.next = Node(15)
head.next.next.next.next = Node(20)
head.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next = Node(4)
head.next.next.next.next.next.next.next = Node(1)
head.next.next.next.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next.next.next.next.next = Node(10)

print_LL(head)
print("\n")
print_LL(myfun(head))
