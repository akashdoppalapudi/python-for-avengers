class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        if len(self.stack) or self.stack:
            a = list(map(str, self.stack)) 
            return ' '.join(a)
        return "Stack Underflow"

    def __del__(self):
        print("stack is deleted successfully")

    def PUSH(self, val):
        self.stack.insert(0,val)

    def POP(self):
        if len(self.stack) or self.stack:
            self.stack.pop(0)
        else:
            print("stack UnderFlow")


s = Stack()
s.PUSH(2)
s.PUSH(5)
s.PUSH(11)
s.PUSH("Akash")
s.PUSH(19)
print(s)
s.POP()
print(s)