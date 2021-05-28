class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def formLink(self, next):
        self.next = next

    

node1 = Node(5)
node2 = Node(6)
node1.formLink(node2)

print(node1.next.next)