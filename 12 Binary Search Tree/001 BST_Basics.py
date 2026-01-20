# ============================================================
#            BINARY SEARCH TREE (BST) – BASICS
# ============================================================

# A Binary Search Tree is a special type of Binary Tree
# that follows a STRICT PROPERTY.

# ============================================================
#            BST PROPERTY (MOST IMPORTANT)
# ============================================================

# For every node:
# - Left subtree contains values < node.data
# - Right subtree contains values > node.data
# - Both left & right subtrees are also BSTs

# ============================================================
#            WHY BST?
# ============================================================

# Advantages:
# ✅ Faster search than normal Binary Tree
# ✅ Sorted data access using inorder traversal
# ✅ Efficient insert & delete (average case)

# Time Complexity (average):
# Search / Insert / Delete → O(log n)

# Worst case (skewed tree):
# O(n)

# ============================================================
#            BST vs BINARY TREE
# ============================================================

# Binary Tree:
# - No ordering
# - Search → O(n)

# BST:
# - Ordered
# - Search → O(log n) average

# ============================================================
#            COMMON MISTAKES
# ============================================================

# 1. Forgetting BST property
# 2. Ignoring skewed tree case
# 3. Incorrect delete logic (2 children case)
# 4. Not using inorder successor properly

# ============================================================
#            THINKING RULE (INTERVIEW GOLD)
# ============================================================

# If a problem involves:
# - Sorted data
# - Fast search
# - Range queries
# 👉 THINK BST

# ============================================================
# End of File: 001 Binary_Search_Tree_Basics.py
# ============================================================
