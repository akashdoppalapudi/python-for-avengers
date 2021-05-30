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

    def addNode(self, val, pos=-1):
        new_node = Node(val)
        node = self
        if pos == -1:
            while(node.next!=None):
                node = node.next

            node.formLink(new_node)

        elif pos>0:
            i = 1
            try:
                while(i<pos):
                    node = node.next
                    i += 1

                next_node = node.next
                node.formLink(new_node)
                new_node.formLink(next_node)
            
            except AttributeError:
                print("Invalid Position")
        
        else:
            print("Invalid Position")

    def length(self):
        i = 0
        node = self
        while(node!=None):
            node = node.next
            i += 1
        return i
    
    def removeNode(self, pos=-1):
        node = self
        if pos == -1:
            while (node.next.next!=None):
                node = node.next
            del node.next
            node.next = None
        
        elif pos>0:
            i = 1
            try:
                while(i<pos):
                    node = node.next
                    i += 1
                node.formLink(node.next.next)
            except AttributeError:
                print("Invalid Position")
        
        else:
            print("Invalid Position")



root = Node().convert([4,6,5,8,9,8,2])
root.display()

root.removeNode()

root.display()