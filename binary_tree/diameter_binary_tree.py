class Solution:

    def height(self, root, res):
        if not root:
            return 0
        lh = self.height(root.left, res)
        rh = self.height(root.right, res)
        res = max(res, lh+rh+1)
        return 1+max(lh, rh)

    # Function to return the diameter of a Binary Tree.
    def diameter(self, root):
        # Code here
        if not root:
            return 0
        d1 = 1+self.height(root.left, res=0) + self.height(root.right, res=0)

        d2 = self.diameter(root.left)
        d3 = self.diameter(root.right)

        return max(d1, max(d2, d3))
