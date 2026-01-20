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
#            INORDER TRAVERSAL (SORTED ORDER)
# ============================================================

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

# ============================================================
#            PREORDER TRAVERSAL
# ============================================================

def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

# ============================================================
#            POSTORDER TRAVERSAL
# ============================================================

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")

# ============================================================
#            FIND MINIMUM VALUE (LEFTMOST NODE)
# ============================================================

def find_min(root):
    current = root
    while current.left:
        current = current.left
    return current.data

# ============================================================
#            FIND MAXIMUM VALUE (RIGHTMOST NODE)
# ============================================================

def find_max(root):
    current = root
    while current.right:
        current = current.right
    return current.data

# ============================================================
#            DELETE NODE FROM BST
# ============================================================

def delete(root, key):
    if root is None:
        return root

    if key < root.data:
        root.left = delete(root.left, key)

    elif key > root.data:
        root.right = delete(root.right, key)

    else:
        # Case 1: No child
        if root.left is None and root.right is None:
            return None

        # Case 2: One child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Case 3: Two children
        # Replace with inorder successor
        successor = find_min(root.right)
        root.data = successor
        root.right = delete(root.right, successor)

    return root

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