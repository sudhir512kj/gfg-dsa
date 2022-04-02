class Solution:
    # Function to return the lowest common ancestor in a Binary Tree.
    def lca(self, root, n1, n2):
        # Code here
        if not root:
            return None
        if root.data == n1 or root.data == n2:
            return root

        lca1 = self.lca(root.left, n1, n2)
        lca2 = self.lca(root.right, n1, n2)

        if lca1 and lca2:
            return root
        if lca1:
            return lca1
        else:
            return lca2
