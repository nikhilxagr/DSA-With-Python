# ============================================================
#            DATA STRUCTURES OVERVIEW IN PYTHON
# ============================================================

# Data Structures are ways to:
# - Store data
# - Organize data
# - Access data efficiently

# Choosing the RIGHT data structure
# = Faster programs + Less memory usage

# ============================================================
#            WHY DATA STRUCTURES ARE IMPORTANT
# ============================================================

# 1. Improve performance
# 2. Optimize memory usage
# 3. Essential for DSA & interviews
# 4. Used in real-world systems
# 5. Core skill for software & security engineers

# ============================================================
#            TYPES OF DATA STRUCTURES
# ============================================================

# 1. Primitive Data Structures
# 2. Non-Primitive Data Structures

# ============================================================
#            DATA STRUCTURES CLASSIFICATION
# ============================================================

# +--------------------+--------------------------------------+
# | Category           | Examples                             |
# +--------------------+--------------------------------------+
# | Primitive          | int, float, char, bool               |
# | Linear             | List, Tuple, Stack, Queue            |
# | Non-Linear         | Tree, Graph                          |
# | Hash-Based         | Dictionary, Set                      |
# +--------------------+--------------------------------------+

# ============================================================
#            1. PRIMITIVE DATA STRUCTURES
# ============================================================

# Basic data types that store single values

a = 10          # int
b = 3.14        # float
c = "Python"    # string
d = True        # boolean

# Time Complexity → O(1)
# Space Complexity → O(1)

# ============================================================
#            2. LINEAR DATA STRUCTURES
# ============================================================

# Data stored sequentially

# ============================================================
#            LIST
# ============================================================

arr = [10, 20, 30, 40]

# Characteristics:
# - Ordered
# - Mutable
# - Allows duplicates

# Access → O(1)
# Search → O(n)
# Insert/Delete → O(n)

# ============================================================
#            TUPLE
# ============================================================

tup = (10, 20, 30)

# Characteristics:
# - Ordered
# - Immutable
# - Faster than list

# Access → O(1)
# Search → O(n)

# ============================================================
#            STACK (LIFO)
# ============================================================

# Last In First Out

stack = []

stack.append(10)   # Push
stack.append(20)
stack.append(30)

print(stack.pop())  # Pop → 30

# Push → O(1)
# Pop  → O(1)

# ============================================================
#            QUEUE (FIFO)
# ============================================================

# First In First Out

from collections import deque

queue = deque()

queue.append(10)      # Enqueue
queue.append(20)
queue.append(30)

print(queue.popleft())  # Dequeue → 10

# Enqueue → O(1)
# Dequeue → O(1)

# ============================================================
#            3. NON-LINEAR DATA STRUCTURES
# ============================================================

# Data is NOT stored sequentially

# ============================================================
#            TREE (CONCEPT)
# ============================================================

# Tree structure:
#        A
#      /   \
#     B     C
#    / \
#   D   E

# Used in:
# - File systems
# - Databases
# - HTML DOM
# - Search algorithms

# ============================================================
#            GRAPH (CONCEPT)
# ============================================================

# Graph consists of:
# - Nodes (vertices)
# - Edges (connections)

# Used in:
# - Social networks
# - Network routing
# - Maps & navigation
# - Cybersecurity graphs

# ============================================================
#            4. HASH-BASED DATA STRUCTURES
# ============================================================

# ============================================================
#            DICTIONARY (HASH MAP)
# ============================================================

data = {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}

# Characteristics:
# - Key : Value pairs
# - Unordered (logically)
# - Fast lookup

# Search → O(1)
# Insert → O(1)
# Delete → O(1)

# ============================================================
#            SET
# ============================================================

unique_numbers = {1, 2, 3, 4}

# Characteristics:
# - Unordered
# - No duplicates

# Search → O(1)
# Insert → O(1)

# ============================================================
#            DATA STRUCTURES COMPARISON TABLE
# ============================================================

# +------------+-----------+-----------+-----------+----------+
# | Structure  | Ordered   | Mutable   | Search    | Access   |
# +------------+-----------+-----------+-----------+----------+
# | List       | Yes       | Yes       | O(n)      | O(1)     |
# | Tuple      | Yes       | No        | O(n)      | O(1)     |
# | Set        | No        | Yes       | O(1)      | ❌       |
# | Dict       | No        | Yes       | O(1)      | ❌       |
# | Stack      | Yes       | Yes       | O(n)      | O(1)     |
# | Queue      | Yes       | Yes       | O(n)      | O(1)     |
# +------------+-----------+-----------+-----------+----------+

# ============================================================
#            REAL-LIFE USE CASES
# ============================================================

# List        → To-do lists, logs
# Stack       → Undo / Redo operations
# Queue       → Task scheduling, buffering
# Dictionary → Database records
# Set         → Removing duplicates
# Tree        → File systems
# Graph       → Networks, cybersecurity maps

# ============================================================
#            HOW TO CHOOSE RIGHT DATA STRUCTURE
# ============================================================

# If you need fast lookup → Dictionary / Set
# If order matters        → List / Tuple
# If LIFO behavior        → Stack
# If FIFO behavior        → Queue
# If hierarchy            → Tree
# If relationships        → Graph

# ============================================================
#            COMMON MISTAKES
# ============================================================

# 1. Using list instead of set for membership checks
# 2. Using dictionary when list is enough
# 3. Ignoring time & space complexity
# 4. Over-complicating data structures

# ============================================================
#            IMPORTANT POINTS
# ============================================================

# 1. Data Structures + Algorithms = DSA
# 2. Choice of DS affects performance
# 3. Python provides powerful built-in DS
# 4. Interviews focus heavily on DS usage
# 5. Master basics before advanced DS

# ============================================================
# End of File: 029 Data_Structures_Overview.py
# ============================================================
