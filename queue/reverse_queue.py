from queue import Queue


def reverse_queue(q: Queue):
    s = []
    while not q.empty():
        s.append(q.queue[0])
        q.get()
    while s:
        q.put(s[-1])
        s.pop()


def print_queue(queue: Queue):
    while not queue.empty():
        print(queue.queue[0], end=" ")
        queue.get()
    print()


# Driver Code
if __name__ == "__main__":
    q = Queue()
    q.put(56)
    q.put(27)
    q.put(30)
    q.put(45)
    q.put(85)
    q.put(92)
    q.put(58)
    q.put(80)
    q.put(90)
    q.put(100)

    reverse_queue(q)
    print_queue(q)
