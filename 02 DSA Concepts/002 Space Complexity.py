# ============================================================
#               SPACE COMPLEXITY IN PYTHON
# ============================================================

# Space Complexity measures:
# - How much MEMORY an algorithm uses
#   with respect to input size (n)

# It includes:
# 1. Input space
# 2. Auxiliary (extra) space

# ============================================================
#               WHY SPACE COMPLEXITY MATTERS
# ============================================================

# 1. Prevents memory overflow
# 2. Important for large-scale systems
# 3. Required for efficient algorithms
# 4. Critical in embedded & security systems
# 5. Asked in interviews & DSA rounds

# ============================================================
#               SPACE COMPLEXITY BASICS
# ============================================================

# Space Complexity focuses on:
# - Variables
# - Data structures
# - Function call stack (recursion)

# Represented using Big-O notation:
# O(1), O(n), O(n²), O(log n), etc.

# ============================================================
#               SPACE COMPLEXITY SUMMARY TABLE
# ============================================================

# +--------------+----------------------------+-------------------+
# | Big-O        | Name                       | Example           |
# +--------------+----------------------------+-------------------+
# | O(1)         | Constant Space             | Few variables     |
# | O(n)         | Linear Space               | Extra list        |
# | O(n²)        | Quadratic Space            | 2D matrix        |
# | O(log n)     | Logarithmic Space          | Recursion stack  |
# +--------------+----------------------------+-------------------+

# ============================================================
#               O(1) — CONSTANT SPACE
# ============================================================

# Uses fixed amount of memory
# Memory does NOT grow with input size

def sum_two_numbers(a, b):
    result = a + b
    return result

print(sum_two_numbers(10, 20))

# Space Complexity → O(1)

# ============================================================
#               O(n) — LINEAR SPACE
# ============================================================

# Extra memory grows with input size

def copy_list(arr):
    new_arr = []
    for x in arr:
        new_arr.append(x)
    return new_arr

print(copy_list([1, 2, 3, 4, 5]))

# Space Complexity → O(n)

# ============================================================
#               O(n²) — QUADRATIC SPACE
# ============================================================

# Using 2D data structures

def create_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        matrix.append(row)
    return matrix

print(create_matrix(3))

# Space Complexity → O(n²)

# ============================================================
#               O(log n) — LOGARITHMIC SPACE
# ============================================================

# Common in recursive algorithms like Binary Search

def binary_search(arr, left, right, target):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, left, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, right, target)

# Space Complexity → O(log n) (due to recursion stack)

# ============================================================
#               SPACE IN RECURSION
# ============================================================

# Recursive calls consume stack memory

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Space Complexity → O(n) (call stack)

# ============================================================
#               IN-PLACE ALGORITHMS
# ============================================================

# In-place algorithms use NO extra space
# They modify the input directly

def reverse_list(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

nums = [1, 2, 3, 4]
reverse_list(nums)
print(nums)

# Space Complexity → O(1)

# ============================================================
#               SPACE COMPLEXITY OF DATA STRUCTURES
# ============================================================

# LIST      → O(n)
# TUPLE     → O(n)
# SET       → O(n)
# DICTIONARY→ O(n)
# STRING    → O(n)

# ============================================================
#               INPUT SPACE vs AUXILIARY SPACE
# ============================================================

# Input Space:
# Memory used by input itself

# Auxiliary Space:
# Extra memory used by algorithm (excluding input)

# Example:
def square_elements(arr):
    result = []
    for x in arr:
        result.append(x * x)
    return result

# Input Space → O(n)
# Auxiliary Space → O(n)

# ============================================================
#               OPTIMIZED VERSION (LESS SPACE)
# ============================================================

def square_in_place(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] * arr[i]
    return arr

# Auxiliary Space → O(1)

# ============================================================
#               REAL-LIFE EXAMPLES
# ============================================================

# ------------------------------------------------------------
# Example 1: Sum of elements
# ------------------------------------------------------------

def sum_elements(arr):
    total = 0
    for x in arr:
        total += x
    return total

# Space Complexity → O(1)

# ------------------------------------------------------------
# Example 2: Remove duplicates
# ------------------------------------------------------------

def remove_duplicates(arr):
    return list(set(arr))

# Space Complexity → O(n)

# ============================================================
#               TIME vs SPACE TRADE-OFF
# ============================================================

# Sometimes:
# - Faster code uses more memory
# - Memory-efficient code is slower

# Example:
# Using set → Faster search but more memory
# Using list → Less memory but slower search

# ============================================================
#               COMMON MISTAKES
# ============================================================

# 1. Ignoring recursion stack space
# 2. Confusing input space with auxiliary space
# 3. Thinking in-place means no memory usage
# 4. Forgetting hidden memory usage of data structures

# ============================================================
#               IMPORTANT POINTS
# ============================================================

# 1. Space Complexity measures memory growth
# 2. Auxiliary space is key in optimization
# 3. O(1) space is best
# 4. Recursion increases space usage
# 5. Always balance time & space

# ============================================================
# End of File: 028 Space_Complexity.py
# ============================================================
