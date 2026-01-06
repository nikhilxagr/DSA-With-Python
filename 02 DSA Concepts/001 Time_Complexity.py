# ============================================================
#               TIME COMPLEXITY IN PYTHON
# ============================================================

# Time Complexity measures:
# - How the execution time of an algorithm
#   grows with respect to input size (n)

# It DOES NOT measure actual seconds,
# but growth rate as input increases.

# ============================================================
#               WHY TIME COMPLEXITY MATTERS
# ============================================================

# 1. Helps write efficient code
# 2. Important for interviews (DSA)
# 3. Prevents slow programs
# 4. Required for competitive programming
# 5. Used in real-world system design

# ============================================================
#               BIG-O NOTATION
# ============================================================

# Big-O describes the WORST-CASE performance

# Examples:
# O(1)     → Constant time
# O(log n) → Logarithmic time
# O(n)     → Linear time
# O(n log n)
# O(n²)    → Quadratic time
# O(2ⁿ)    → Exponential time

# ============================================================
#               TIME COMPLEXITY SUMMARY TABLE
# ============================================================

# +--------------+-----------------------------+--------------------+
# | Big-O        | Name                        | Example            |
# +--------------+-----------------------------+--------------------+
# | O(1)         | Constant                    | Access by index    |
# | O(log n)     | Logarithmic                 | Binary search      |
# | O(n)         | Linear                      | Loop               |
# | O(n log n)   | Linearithmic                | Merge sort         |
# | O(n²)        | Quadratic                   | Nested loops       |
# | O(2ⁿ)        | Exponential                 | Recursion (bad)    |
# +--------------+-----------------------------+--------------------+

# ============================================================
#               O(1) — CONSTANT TIME
# ============================================================

# Time does NOT depend on input size

arr = [10, 20, 30, 40]

print(arr[0])     # Always takes same time
print(arr[-1])

# Time Complexity → O(1)

# ============================================================
#               O(n) — LINEAR TIME
# ============================================================

# Time grows linearly with input size

def print_elements(arr):
    for x in arr:
        print(x)

print_elements([1, 2, 3, 4, 5])

# Time Complexity → O(n)

# ============================================================
#               O(n²) — QUADRATIC TIME
# ============================================================

# Nested loops

def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)

print_pairs([1, 2, 3])

# Time Complexity → O(n²)

# ============================================================
#               O(log n) — LOGARITHMIC TIME
# ============================================================

# Binary Search (sorted list)

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Time Complexity → O(log n)

# ============================================================
#               O(n log n)
# ============================================================

# Common in efficient sorting algorithms
# Example: Merge Sort, Quick Sort (average)

# Python's built-in sort()
numbers = [5, 2, 9, 1, 3]
numbers.sort()

# Time Complexity → O(n log n)

# ============================================================
#               O(2ⁿ) — EXPONENTIAL TIME
# ============================================================

# Very slow — avoid if possible

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Time Complexity → O(2ⁿ)

# ============================================================
#               O(n!) — FACTORIAL TIME
# ============================================================

# Extremely slow
# Example: Generating all permutations

# Used only for very small inputs

# ============================================================
#               TIME COMPLEXITY OF COMMON OPERATIONS
# ============================================================

# LIST:
# Access element → O(1)
# Search element → O(n)
# Insert at end  → O(1)
# Insert at start → O(n)

# DICTIONARY:
# Search key     → O(1)
# Insert key     → O(1)
# Delete key     → O(1)

# SET:
# Search         → O(1)
# Insert         → O(1)

# ============================================================
#               BEST, WORST & AVERAGE CASE
# ============================================================

# Best Case    → Minimum time
# Average Case → Expected time
# Worst Case   → Maximum time (Big-O focuses on this)

# Example: Linear search
# Best Case    → Element at first index → O(1)
# Worst Case   → Element at last index → O(n)

# ============================================================
#               HOW TO CALCULATE TIME COMPLEXITY
# ============================================================

# Rule 1: Ignore constants
# O(2n) → O(n)

# Rule 2: Ignore lower order terms
# O(n² + n) → O(n²)

# Rule 3: Nested loops multiply
# Loop inside loop → O(n²)

# ============================================================
#               REAL-LIFE EXAMPLES
# ============================================================

# ------------------------------------------------------------
# Example 1: Find max element
# ------------------------------------------------------------

def find_max(arr):
    max_val = arr[0]
    for x in arr:
        if x > max_val:
            max_val = x
    return max_val

# Time Complexity → O(n)

# ------------------------------------------------------------
# Example 2: Check duplicates
# ------------------------------------------------------------

def has_duplicates(arr):
    seen = set()
    for x in arr:
        if x in seen:
            return True
        seen.add(x)
    return False

# Time Complexity → O(n)

# ============================================================
#               COMMON MISTAKES
# ============================================================

# 1. Thinking Big-O is exact time
# 2. Ignoring nested loops
# 3. Forgetting worst-case analysis
# 4. Using inefficient algorithms for large input

# ============================================================
#               IMPORTANT POINTS
# ============================================================

# 1. Big-O focuses on growth rate
# 2. Smaller Big-O is better
# 3. O(1) is best, O(n²) is bad for large n
# 4. Use built-in data structures wisely
# 5. Optimization matters at scale

# ============================================================
# End of File: 027 Time_Complexity.py
# ============================================================
