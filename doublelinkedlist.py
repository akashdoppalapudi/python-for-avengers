class Dnode:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def display(self):
        if self.next!=None:
            node = self
            while(node!=None):
                print(node.val, "<--> ", end="")
                node = node.next
            print(None)
        else:
            print("Linked list cant be printed when given last node")

    def formLink(self, new_node):
        self.next = new_node
        new_node.prev = self

    def convert(self, l):
        nodes = []
        nodes.append(Dnode(l[0]))
        for i in range(1, len(l)):
            nodes.append(Dnode(l[i]))
            nodes[i-1].formLink(nodes[i])

        return nodes[0], nodes[-1]

    def length(self):
        if self.prev==None:
            i = 0
            node = self
            while(node!=None):
                node = node.next
                i += 1
            return i
        else:
            print("First node should be given to find length.")
