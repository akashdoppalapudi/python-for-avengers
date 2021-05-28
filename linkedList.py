class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def formLink(self, next):
        self.next = next

    def display(self):
        node = self
        while(node!=None):
            print(node.val, "--> ", end="")
            node = node.next
        print(None)

    def convert(self, l):
        nodes = []
        nodes.append(Node(l[0]))
        for i in range(1,len(l)):
            nodes.append(Node(l[i]))
            nodes[i-1].formLink(nodes[i])

        return nodes[0]
    