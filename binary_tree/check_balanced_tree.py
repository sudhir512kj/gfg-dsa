# Function to check whether a binary tree is balanced or not.
class Solution:
    def isBalanced(self, root):

        # add code here
        if not root:
            return 0
        lh = self.isBalanced(root.left)
        if lh == -1:
            return -1
        rh = self.isBalanced(root.right)
        if rh == -1:
            return -1
        if abs(lh-rh) > 1:
            return -1
        else:
            return max(lh, rh)+1
