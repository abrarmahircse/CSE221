class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.size = 1  

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    root.size = 1 + get_size(root.left) + get_size(root.right)
    return root

def get_size(node):
    return node.size if node else 0

def count_less(root, val):
    if root is None:
        return 0
    if val <= root.val:
        return count_less(root.left, val)
    else:
        return 1 + get_size(root.left) + count_less(root.right, val)

n = int(input())
A = list(map(int, input().split()))

root = None
ans = 0

for i in reversed(range(n)):
    ans += count_less(root, A[i])
    root = insert(root, A[i] ** 2)

print(ans)
