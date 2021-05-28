class Queue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        if len(self.queue) or self.queue:
            a = list(map(str, self.queue))
            return ' '.join(a)
        return "Queue Underflow"

    def __del__(self):
        print("queue is deleted successfully")

    def PUSH(self, val):
        self.queue.insert(0, val)

    def POP(self):
        if len(self.queue) or self.queue:
            self.queue.pop(-1)
        else:
            print("Queue Underflow")


q1 = Queue()
q1.PUSH(3)
q1.PUSH(5)
q1.PUSH(6)
print(q1)
q1.POP()
print(q1)