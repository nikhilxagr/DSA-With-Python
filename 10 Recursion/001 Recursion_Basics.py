# ============================================================
#                   RECURSION – BASICS (PYTHON)
# ============================================================

# Recursion is a technique where:
# A function calls itself to solve a smaller subproblem

# ============================================================
#                   WHY RECURSION?
# ============================================================

# Used in:
# - Tree traversal
# - Graph traversal (DFS)
# - Backtracking
# - Divide & Conquer
# - Dynamic Programming

# ============================================================
#                   RECURSION HAS TWO PARTS
# ============================================================

# 1. BASE CASE  → Stops recursion
# 2. RECURSIVE CASE → Function calls itself

# Without base case → INFINITE RECURSION ❌

# ============================================================
#                   BASIC RECURSION FLOW
# ============================================================

# f(n) → f(n-1) → f(n-2) → ... → f(0)
# then returns back (stack unwinding)

# ============================================================
#                   SIMPLE EXAMPLE
# ============================================================

def print_numbers(n):
    if n == 0:            # Base case
        return
    print(n)
    print_numbers(n - 1)  # Recursive call

print_numbers(5)

# ============================================================
#                   RECURSION TREE (CONCEPT)
# ============================================================

# print_numbers(3)
#   print(3)
#   print_numbers(2)
#       print(2)
#       print_numbers(1)
#           print(1)
#           print_numbers(0) -> stop

# ============================================================
#                   FACTORIAL (CLASSIC)
# ============================================================

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# Time → O(n)
# Space → O(n) (call stack)

# ============================================================
#                   SUM OF N NUMBERS
# ============================================================

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(5))

# ============================================================
#                   PRINT 1 TO N
# ============================================================

def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n)

print_1_to_n(5)

# ============================================================
#                   FIBONACCI (BASIC)
# ============================================================

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))

# Time → O(2^n) ❌ (inefficient)
# Used to understand recursion, NOT for performance

# ============================================================
#                   CHECK PALINDROME (RECURSION)
# ============================================================

def is_palindrome(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return is_palindrome(s, left + 1, right - 1)

print(is_palindrome("radar", 0, len("radar") - 1))
print(is_palindrome("python", 0, len("python") - 1))

# ============================================================
#                   REVERSE STRING (RECURSION)
# ============================================================

def reverse_string(s):
    if s == "":
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))

# ============================================================
#                   COUNT DIGITS (RECURSION)
# ============================================================

def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

print(count_digits(12345))

# ============================================================
#                   IMPORTANT RULES (MUST REMEMBER)
# ============================================================

# 1. Always define base case FIRST
# 2. Ensure problem size reduces
# 3. Trust recursion
# 4. Draw recursion tree
# 5. Watch stack space

# ============================================================
#                   COMMON MISTAKES
# ============================================================

# ❌ Missing base case
# ❌ Not reducing problem size
# ❌ Expecting recursion to be faster always
# ❌ Stack overflow for large inputs

# ============================================================
#                   WHEN TO USE RECURSION?
# ============================================================

# ✔ Tree / Graph problems
# ✔ Divide & Conquer
# ✔ Backtracking
# ✔ When problem is naturally recursive

# ============================================================
#                   WHEN NOT TO USE?
# ============================================================

# ❌ Very deep recursion (Python limit ~1000)
# ❌ Simple loops are better
# ❌ Performance-critical code

# ============================================================
#                   ITERATION vs RECURSION
# ============================================================

# Iteration:
# - Faster
# - Less memory

# Recursion:
# - Cleaner logic
# - Easier for complex problems

# ============================================================
# End of File: 001 Recursion_Basics.py
# ============================================================
