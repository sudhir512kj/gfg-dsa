class Node:
    def __init__(self, val) -> None:
        self.data = val
        self.next = None


class QueueLL:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, x):
        temp = Node(x)
        self.size += 1
        if not self.front:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def dequeue(self):
        if not self.front:
            return
        self.size += 1
        temp = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        del temp


q = QueueLL()
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.enqueue(4)
q.dequeue()
print(q.front.data)
print(q.rear.data)
