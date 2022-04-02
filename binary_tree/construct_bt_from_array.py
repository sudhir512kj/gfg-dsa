from queue import Queue


class Node:
    def __init__(self, k) -> None:
        self.data = k
        self.left = self.right = None

def levelOrder(root):
    # Code here
    if not root:
        return
    q = Queue()
    q.put(root)
    res = []

    while not q.empty():
        curr = q.queue[0]
        q.get()
        res.append(curr.data)
        if curr.left:
            q.put(curr.left)
        if curr.right:
            q.put(curr.right)

    return res

# Function to construct binary tree from parent array.
def createTree(parent, N, i):
    if i == N:
        return None
    val = parent[i]
    i += 1

    if val == -1:
        return None

    root = Node(val)
    root.left = createTree(parent, N, i)
    root.right = createTree(parent, N, i)
    return root

root = createTree([-1, 0, 0, 1, 1, 3, 5], 7, i=0)
print(levelOrder(root))
