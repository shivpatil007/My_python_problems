class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkList:
    def __init__(self) -> None:
        self.head = None

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()
    
    def reverse_every_n_nodes(self,n):
        prev = None
        current = self.head
        i=0
        while current is not None and i<n:
            next = current.next
            current.next = prev
            prev = current
            current = next
            i+=1
        if next is not None:
            self.head.next = self.reverse_every_n_nodes(next,n)
        return prev
        