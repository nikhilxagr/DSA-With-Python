from traversal import inorder, preorder, postorder
from findMinmax import find_min, find_max
from deletion import delete

# ============================================================
#            BST NODE STRUCTURE
# ============================================================

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# ============================================================
#            INSERT INTO BST
# ============================================================

def insert(root, key):
    # Base case: empty spot found
    if root is None:
        return BSTNode(key)

    if key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)

    return root

# ============================================================
#            SEARCH IN BST
# ============================================================

def search(root, key):
    if root is None:
        return False

    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)

# ============================================================
#            CREATE & TEST BST
# ============================================================

root = None
values = [50, 30, 70, 20, 40, 60, 80]

for v in values:
    root = insert(root, v)

print("Inorder (Sorted):")
inorder(root)

print("\nPreorder:")
preorder(root)

print("\nPostorder:")
postorder(root)

print("\nSearch 40:", search(root, 40))
print("Search 100:", search(root, 100))

print("Minimum:", find_min(root))
print("Maximum:", find_max(root))

print("\nDelete 50 (root):")
root = delete(root, 50)
inorder(root)