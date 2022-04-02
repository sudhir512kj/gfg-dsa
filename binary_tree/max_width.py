from queue import Queue


class Solution:
    # Function to get the maximum width of a binary tree.
    def getMaxWidth(self, root):

        # code here
        if not root:
            return 0

        q = Queue()
        q.put(root)
        res = 0

        while not q.empty():
            count = q.qsize()
            res = max(res, count)

            for i in range(count):
                curr = q.queue[0]
                q.get()
                if curr.left:
                    q.put(curr.left)
                if curr.right:
                    q.put(curr.right)

        return res
