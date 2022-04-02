# Function to return a list containing elements of left view of the binary tree.
from queue import Queue


def LeftView(root):

    # code here
    res = []

    if not root:
        return []

    q = Queue()
    q.put(root)

    while not q.empty():
        count = q.qsize()
        for i in range(count):
            curr = q.queue[0]
            q.get()

            if i == 0:
                res.append(curr.data)
            if curr.left:
                q.put(curr.left)
            if curr.right:
                q.put(curr.right)

    return res
