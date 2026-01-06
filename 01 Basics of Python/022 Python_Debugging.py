# ============================================================
#                 PYTHON DEBUGGING
# ============================================================

# Debugging is the process of:
# - Finding errors (bugs)
# - Understanding why they occur
# - Fixing them correctly

# Every programmer spends a LOT of time debugging.
# Learning debugging early = becoming a better developer.

# ============================================================
#               DEBUGGING SUMMARY TABLE
# ============================================================

# +--------------------+--------------------------------------+
# | Term               | Description                          |
# +--------------------+--------------------------------------+
# | Bug                | Error in a program                   |
# | Debugging          | Process of fixing bugs               |
# | Traceback          | Error message showing call stack     |
# | Breakpoint         | Pause execution to inspect code      |
# | Debugger           | Tool to debug code                   |
# +--------------------+--------------------------------------+

# ============================================================
#               TYPES OF ERRORS IN PYTHON
# ============================================================

# 1. Syntax Error      → Code structure is wrong
# 2. Runtime Error     → Error during execution
# 3. Logical Error     → Code runs but wrong output

# ============================================================
#               1. SYNTAX ERRORS
# ============================================================

# ❌ Missing colon
# if x == 5
#     print("Hello")

# ❌ Wrong indentation
# if True:
# print("Error")

# ============================================================
#               2. RUNTIME ERRORS
# ============================================================

# ZeroDivisionError
# print(10 / 0)

# NameError
# print(x)

# TypeError
# print("10" + 5)

# ============================================================
#               3. LOGICAL ERRORS
# ============================================================

# Program runs but gives wrong output

# ❌ Logical error
a = 10
b = 20
print("Sum:", a * b)   # Wrong operator

# ✅ Fixed
print("Correct Sum:", a + b)

# ============================================================
#               USING print() FOR DEBUGGING
# ============================================================

x = 5
y = 10

print("x =", x)
print("y =", y)
print("x + y =", x + y)

# ============================================================
#               READING TRACEBACK MESSAGES
# ============================================================

# Traceback shows:
# - Error type
# - File name
# - Line number
# - Error message

# Example:
# Traceback (most recent call last):
#   File "test.py", line 5
#   ZeroDivisionError: division by zero

# ============================================================
#               TRY-EXCEPT FOR DEBUGGING
# ============================================================

try:
    num = int(input("Enter number: "))
    print(100 / num)
except Exception as e:
    print("Error:", e)

# ============================================================
#               USING assert STATEMENT
# ============================================================

# assert helps catch bugs early

age = 16
assert age >= 18, "Age must be at least 18"

# ============================================================
#               USING pdb (PYTHON DEBUGGER)
# ============================================================

# pdb allows step-by-step execution

# Steps:
# 1. import pdb
# 2. pdb.set_trace()

# Example:

import pdb

def add(a, b):
    pdb.set_trace()   # Debugger starts here
    return a + b

# Uncomment to test
# print(add(5, 3))

# Common pdb commands:
# n  → next line
# s  → step into function
# c  → continue execution
# q  → quit debugger
# p  → print variable

# ============================================================
#               DEBUGGING USING IDE (VS CODE / PYCHARM)
# ============================================================

# IDE Features:
# - Breakpoints
# - Step Over / Step Into
# - Variable inspection
# - Call stack view

# Steps (VS Code):
# 1. Click left of line number (add breakpoint)
# 2. Press F5
# 3. Inspect variables

# ============================================================
#               COMMON DEBUGGING SCENARIOS
# ============================================================

# ------------------------------------------------------------
# Example 1: IndexError
# ------------------------------------------------------------

data = [1, 2, 3]

try:
    print(data[5])
except IndexError:
    print("Index out of range")

# ------------------------------------------------------------
# Example 2: KeyError
# ------------------------------------------------------------

student = {"name": "Rahul"}

try:
    print(student["age"])
except KeyError:
    print("Key not found")

# ------------------------------------------------------------
# Example 3: FileNotFoundError
# ------------------------------------------------------------

try:
    with open("unknown.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File does not exist")

# ============================================================
#               REAL-LIFE DEBUGGING EXAMPLES
# ============================================================

# ------------------------------------------------------------
# Example 1: Login bug
# ------------------------------------------------------------

username = "admin"
password = "1234"

input_user = "admin"
input_pass = "12345"

if input_user == username and input_pass == password:
    print("Login successful")
else:
    print("Login failed")   # Debug logic here

# ------------------------------------------------------------
# Example 2: Wrong average calculation
# ------------------------------------------------------------

marks = [80, 90, 70]
total = sum(marks)
average = total / len(marks)   # Correct logic

print("Average:", average)

# ============================================================
#               DEBUGGING BEST PRACTICES
# ============================================================

# 1. Read error messages carefully
# 2. Reproduce the bug consistently
# 3. Debug small sections at a time
# 4. Use print(), assert, and pdb
# 5. Fix root cause, not symptoms

# ============================================================
#               COMMON MISTAKES
# ============================================================

# 1. Ignoring traceback
# 2. Randomly changing code
# 3. Not testing edge cases
# 4. Overusing print debugging

# ============================================================
#               IMPORTANT POINTS
# ============================================================

# 1. Bugs are normal in programming
# 2. Debugging is a skill, not a talent
# 3. pdb is very powerful
# 4. Assertions help catch bugs early
# 5. Good debugging = clean code

# ============================================================
# End of File: 022 Python_Debugging.py
# ============================================================
