class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def delete_bst(root, key):
    # Base case
    if root is None:
        return root

    # Traverse the tree
    if key < root.key:
        root.left = delete_bst(root.left, key)
    elif key > root.key:
        root.right = delete_bst(root.right, key)
    else:
        # Node with only one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Node with two children:
        # Get inorder successor (smallest in the right subtree)
        successor = min_value_node(root.right)
        root.key = successor.key
        root.right = delete_bst(root.right, successor.key)

    return root


def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current
