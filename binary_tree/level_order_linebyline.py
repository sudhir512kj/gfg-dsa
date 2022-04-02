from queue import Queue

# Function to return the level order traversal line by line of a tree.


def levelOrder(root):

    # code here
    if not root:
        return
    q = Queue()
    q.put(root)
    res = []

    while not q.empty():
        count = q.qsize()
        temp = []
        for i in range(count):
            curr = q.queue[0]
            q.get()
            temp.append(curr.data)
            if curr.left:
                q.put(curr.left)
            if curr.right:
                q.put(curr.right)
        res.append(temp)
    return res
