from queue import Queue


class Solution:
    # Function to return list containing elements of right view of binary tree.
    def rightView(self, root):

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
                if curr.right:
                    q.put(curr.right)
                if curr.left:
                    q.put(curr.left)

        return res
