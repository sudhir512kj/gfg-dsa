class Solution:
    # Function to find the height of a binary tree.
    def height(self, root):
        # code here
        if not root:
            return 0
        else:
            return 1+max(self.height(root.left), self.height(root.right))
