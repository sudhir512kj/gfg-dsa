from queue import Queue


class Solution:
    # Function to return the level order traversal of a tree.
    def levelOrder(self, root):
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
