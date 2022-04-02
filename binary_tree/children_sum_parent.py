class Solution:
    # Function to check whether all nodes of a tree have the value
    # equal to the sum of their child nodes.
    def isSumProperty(self, root):
        # code here
        if not root:
            return 1
        if not root.left and not root.right:
            return 1
        sum = 0
        if root.left:
            sum += root.left.data
        if root.right:
            sum += root.right.data

        return 1 if (root.data == sum and self.isSumProperty(root.left) and self.isSumProperty(root.right)) else 0
