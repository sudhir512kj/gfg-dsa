# Function to return a list containing the level order traversal in spiral form.
class Node:
    def __init__(self, k) -> None:
        self.data = k
        self.left = self.right = None


def findSpiral(root):
    # Code here
    if not root:
        return []

    s1 = []
    s2 = []
    res = []

    s1.append(root)

    while s1 or s2:
        while s2:
            temp = s2[-1]
            s2.pop()
            res.append(temp.data)

            if temp.right:
                s1.append(temp.right)
            if temp.left:
                s1.append(temp.left)

        while s1:
            temp = s1[-1]
            s1.pop()
            res.append(temp.data)

            if temp.left:
                s2.append(temp.left)
            if temp.right:
                s2.append(temp.right)

    return res


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
root.right.left.left = Node(60)
root.right.left.right = Node(70)
root.right.right.right = Node(80)
print(findSpiral(root))
