# ============================================================
#               ALGORITHMS BASICS IN PYTHON
# ============================================================

# An ALGORITHM is a step-by-step procedure
# to solve a specific problem.

# In simple words:
# Algorithm = Logic + Steps + Efficiency

# ============================================================
#               WHY ALGORITHMS ARE IMPORTANT
# ============================================================

# 1. Solve problems efficiently
# 2. Improve time & space complexity
# 3. Core requirement for DSA & interviews
# 4. Used in real-world systems
# 5. Essential for competitive programming

# ============================================================
#               ALGORITHM CHARACTERISTICS
# ============================================================

# 1. Input        → Takes input
# 2. Output       → Produces output
# 3. Definiteness → Clear & unambiguous steps
# 4. Finiteness  → Must terminate
# 5. Effectiveness → Steps must be executable

# ============================================================
#               TYPES OF ALGORITHMS
# ============================================================

# +----------------------+------------------------------------+
# | Type                 | Examples                           |
# +----------------------+------------------------------------+
# | Searching             | Linear Search, Binary Search       |
# | Sorting               | Bubble, Selection, Merge, Quick   |
# | Recursive             | Factorial, Fibonacci              |
# | Greedy                | Coin Change, Activity Selection   |
# | Divide & Conquer      | Merge Sort, Quick Sort             |
# | Dynamic Programming   | Knapsack, Fibonacci (optimized)   |
# +----------------------+------------------------------------+

# ============================================================
#               BASIC ALGORITHM EXAMPLE
# ============================================================

# Problem: Add two numbers

def add(a, b):
    return a + b

print(add(10, 20))

# Time Complexity → O(1)
# Space Complexity → O(1)

# ============================================================
#               ALGORITHM ANALYSIS
# ============================================================

# We analyze algorithms using:
# 1. Time Complexity
# 2. Space Complexity

# Focus is usually on WORST CASE (Big-O)

# ============================================================
#               LINEAR SEARCH ALGORITHM
# ============================================================

# Search element in unsorted list

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

data = [10, 20, 30, 40, 50]
print(linear_search(data, 30))

# Time Complexity:
# Best Case  → O(1)
# Worst Case → O(n)

# ============================================================
#               BINARY SEARCH (CONCEPT)
# ============================================================

# Works ONLY on sorted arrays

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

sorted_data = [10, 20, 30, 40, 50]
print(binary_search(sorted_data, 40))

# Time Complexity → O(log n)

# ============================================================
#               SORTING ALGORITHM (BASIC)
# ============================================================

# Bubble Sort (simple but inefficient)

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

numbers = [5, 3, 8, 1, 2]
bubble_sort(numbers)
print(numbers)

# Time Complexity → O(n²)
# Space Complexity → O(1)

# ============================================================
#               RECURSIVE ALGORITHM
# ============================================================

# Factorial using recursion

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# Time Complexity → O(n)
# Space Complexity → O(n) (call stack)

# ============================================================
#               ITERATIVE vs RECURSIVE
# ============================================================

# Iterative version (better space)

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_iterative(5))

# ============================================================
#               GREEDY ALGORITHM (BASIC IDEA)
# ============================================================

# Always takes the best immediate choice

# Example: Coin Change (concept)

# Coins = [1, 2, 5]
# Amount = 11
# Greedy picks → 5 + 5 + 1

# ============================================================
#               DIVIDE AND CONQUER (CONCEPT)
# ============================================================

# Steps:
# 1. Divide problem
# 2. Solve sub-problems
# 3. Combine results

# Examples:
# - Merge Sort
# - Quick Sort
# - Binary Search

# ============================================================
#               DYNAMIC PROGRAMMING (CONCEPT)
# ============================================================

# Used when:
# - Overlapping subproblems
# - Optimal substructure

# Example: Fibonacci (Optimized)

def fibonacci_dp(n):
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]

print(fibonacci_dp(6))

# Time Complexity → O(n)
# Space Complexity → O(n)

# ============================================================
#               REAL-LIFE ALGORITHM EXAMPLES
# ============================================================

# ------------------------------------------------------------
# Example 1: Find minimum element
# ------------------------------------------------------------

def find_min(arr):
    min_val = arr[0]
    for x in arr:
        if x < min_val:
            min_val = x
    return min_val

print(find_min([4, 2, 7, 1]))

# Time Complexity → O(n)

# ------------------------------------------------------------
# Example 2: Check if list is sorted
# ------------------------------------------------------------

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

print(is_sorted([1, 2, 3, 4]))

# ============================================================
#               COMMON MISTAKES
# ============================================================

# 1. Choosing wrong algorithm
# 2. Ignoring time complexity
# 3. Using recursion without base case
# 4. Sorting when not required

# ============================================================
#               IMPORTANT POINTS
# ============================================================

# 1. Algorithm choice matters more than language
# 2. Simple algorithm ≠ efficient algorithm
# 3. Always analyze time & space complexity
# 4. Practice makes algorithm thinking strong
# 5. Algorithms are foundation of DSA

# ============================================================
# End of File: 030 Algorithms_Basics.py
# ============================================================
