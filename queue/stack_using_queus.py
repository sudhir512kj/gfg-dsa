from queue import Queue


class Stack:
    def __init__(self) -> None:
        self.q1 = Queue()
        self.q2 = Queue()

    def top(self):
        return self.q1.queue[0]

    def size(self):
        return self.q1.qsize()

    def pop(self):
        return self.q1.get()

    def push(self, x):
        while not self.q1.empty():
            self.q2.put(self.q1.queue[0])
            self.q1.get()

        self.q1.put(x)
        while not self.q2.empty():
            self.q1.put(self.q2.queue[0])
            self.q2.get()


s = Stack()
s.push(2)
s.push(3)
print(s.pop())
s.push(4)
print(s.pop())
