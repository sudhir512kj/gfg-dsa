class Node:
    def __init__(self, k) -> None:
        self.key = k
        self.left = self.right = None


def inorderTraversal(root):
    res = []

    def inorder(root, res):
        if root:
            inorder(root.left, res)
            res.append(root.key)
            inorder(root.right, res)
    inorder(root, res)
    return res


def preorderTraversal(root):
    res = []

    def preorder(root, res):
        if root:
            res.append(root.key)
            preorder(root.left, res)
            preorder(root.right, res)
    preorder(root, res)
    return res


def postorderTraversal(root):
    res = []

    def postorder(root, res):
        if root:
            postorder(root.left, res)
            postorder(root.right, res)
            res.append(root.key)
    postorder(root, res)
    return res


def isIdentical(a, b):
    if a is None and b is None:
        return True

    if a is not None and b is not None:
        return ((a.data == b.data) and
                isIdentical(a.left, b.left) and isIdentical(a.right, b.right))

    return False


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
print(inorderTraversal(root))
print(preorderTraversal(root))
print(postorderTraversal(root))
