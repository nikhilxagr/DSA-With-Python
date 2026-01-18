# ============================================================
#                   TREE – INTRODUCTION (PYTHON)
# ============================================================

# A Tree is a NON-LINEAR data structure
# used to represent hierarchical relationships.

# Example (real life):
# - Family tree
# - File system
# - Organization hierarchy
# - HTML DOM

# ============================================================
#                   TREE TERMINOLOGY
# ============================================================

# Root       → Topmost node
# Parent     → Node that has children
# Child      → Node derived from parent
# Leaf       → Node with NO children
# Edge       → Connection between nodes
# Height     → Longest path from node to leaf
# Depth      → Distance from root to node
# Level      → Depth + 1

# ============================================================
#                   TREE STRUCTURE (EXAMPLE)
# ============================================================

#            A
#          /   \
#         B     C
#        / \     \
#       D   E     F

# Root  → A
# Leaf  → D, E, F

# ============================================================
#                   WHY TREES ARE IMPORTANT?
# ============================================================

# 1. Represent hierarchical data
# 2. Faster searching (BST)
# 3. Used in databases & file systems
# 4. Core topic in DSA interviews
# 5. Foundation for graphs

# ============================================================
#                   TYPES OF TREES
# ============================================================

# 1. General Tree
# 2. Binary Tree
# 3. Binary Search Tree (BST)
# 4. AVL Tree
# 5. Heap
# 6. Trie

# In beginning → Focus on BINARY TREE

# ============================================================
#                   BINARY TREE
# ============================================================

# Binary Tree:
# Each node has AT MOST two children
# - Left child
# - Right child

# ============================================================
#                   TREE NODE STRUCTURE
# ============================================================

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# ============================================================
#                   CREATE A SIMPLE TREE
# ============================================================

#        1
#      /   \
#     2     3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# ============================================================
#                   TREE TRAVERSALS
# ============================================================

# Tree traversal = Visiting all nodes

# ============================================================
#                   1. PREORDER (Root → Left → Right)
# ============================================================

def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

# ============================================================
#                   2. INORDER (Left → Root → Right)
# ============================================================

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

# ============================================================
#                   3. POSTORDER (Left → Right → Root)
# ============================================================

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")

# ============================================================
#                   TEST TREE TRAVERSALS
# ============================================================

print("Preorder:")
preorder(root)

print("\nInorder:")
inorder(root)

print("\nPostorder:")
postorder(root)

# ============================================================
#                   TREE TRAVERSAL SUMMARY
# ============================================================

# Preorder  → Used for copying tree
# Inorder   → Sorted order in BST
# Postorder → Used for deleting tree

# ============================================================
#                   TREE HEIGHT (RECURSION)
# ============================================================

def tree_height(root):
    if root is None:
        return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))

print("\nHeight of tree:", tree_height(root))

# ============================================================
#                   NUMBER OF NODES
# ============================================================

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

print("Total nodes:", count_nodes(root))

# ============================================================
#                   TREE IS RECURSIVE
# ============================================================

# Every tree node is a tree itself
# That’s why recursion fits naturally

# ============================================================
#                   TREE TIME COMPLEXITY
# ============================================================

# Traversals → O(n)
# Height     → O(n)
# Count      → O(n)

# ============================================================
#                   COMMON MISTAKES
# ============================================================

# 1. Forgetting base case (None)
# 2. Mixing traversal orders
# 3. Not visualizing tree structure
# 4. Confusing depth & height

# ============================================================
#                   THINKING RULE (VERY IMPORTANT)
# ============================================================

# If problem involves:
# - Hierarchy
# - Parent / child
# - Recursive structure
# 👉 THINK TREE

# ============================================================
# End of File: 067 Tree_Introduction.py
# ============================================================
