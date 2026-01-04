# ============================================================
#                       LOOPS IN PYTHON
# ============================================================

# Loops are used to execute a block of code repeatedly
# until a condition is satisfied or a sequence ends.

# Python supports mainly two types of loops:
# 1. for loop
# 2. while loop

# ============================================================
#                   LOOPS SUMMARY TABLE
# ============================================================

# +------------+---------------------------------------------+
# | Loop Type  | Description                                 |
# +------------+---------------------------------------------+
# | for loop   | Iterates over a sequence (list, range, etc)|
# | while loop | Runs as long as condition is True           |
# +------------+---------------------------------------------+

# ============================================================
#                   1. FOR LOOP
# ============================================================

# Syntax:
# for variable in sequence:
#     code block

# ------------------------------------------------------------
# Example 1: Basic for loop with range()
# ------------------------------------------------------------

for i in range(1, 6):
    print(i)

# ------------------------------------------------------------
# Example 2: for loop with list
# ------------------------------------------------------------

languages = ["Python", "Java", "C++", "JavaScript"]

for lang in languages:
    print(lang)

# ------------------------------------------------------------
# Example 3: for loop with string
# ------------------------------------------------------------

word = "Python"

for char in word:
    print(char)

# ------------------------------------------------------------
# Example 4: range() variations
# ------------------------------------------------------------

# range(start, stop)
for i in range(1, 5):
    print(i)

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)

# ============================================================
#                   NESTED FOR LOOP
# ============================================================

# Loop inside another loop

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# ============================================================
#                   2. WHILE LOOP
# ============================================================

# Syntax:
# while condition:
#     code block

# ------------------------------------------------------------
# Example 1: Basic while loop
# ------------------------------------------------------------

count = 1

while count <= 5:
    print(count)
    count += 1

# ------------------------------------------------------------
# Example 2: while loop with user input
# ------------------------------------------------------------

password = ""

while password != "1234":
    password = input("Enter password: ")

print("Access granted")

# ============================================================
#                   INFINITE LOOP (WARNING)
# ============================================================

# Infinite loop occurs when condition never becomes False
# DO NOT RUN WITHOUT break

# while True:
#     print("This will run forever")

# ============================================================
#                   LOOP CONTROL STATEMENTS
# ============================================================

# ------------------------------------------------------------
# BREAK STATEMENT
# ------------------------------------------------------------

# break exits the loop immediately

for i in range(1, 6):
    if i == 4:
        break
    print(i)

# ------------------------------------------------------------
# CONTINUE STATEMENT
# ------------------------------------------------------------

# continue skips current iteration

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# ------------------------------------------------------------
# PASS STATEMENT
# ------------------------------------------------------------

# pass does nothing (used as placeholder)

for i in range(3):
    if i == 1:
        pass
    print(i)

# ============================================================
#                   LOOP WITH ELSE
# ============================================================

# for-else example
for i in range(3):
    print(i)
else:
    print("for loop completed normally")

# while-else example
x = 0
while x < 3:
    print(x)
    x += 1
else:
    print("while loop completed normally")

# ============================================================
#                   REAL-LIFE EXAMPLES
# ============================================================

# ------------------------------------------------------------
# Example 1: Sum of numbers from 1 to n
# ------------------------------------------------------------

n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum:", total)

# ------------------------------------------------------------
# Example 2: Multiplication table
# ------------------------------------------------------------

num = int(input("Enter number for table: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# ------------------------------------------------------------
# Example 3: Guess the number game
# ------------------------------------------------------------

secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess the number: "))

print("Correct guess!")

# ============================================================
#                   COMMON MISTAKES
# ============================================================

# 1. Forgetting to update loop variable (infinite loop)
# 2. Using wrong indentation
# 3. Using break when continue is needed (and vice versa)

# ============================================================
#                   IMPORTANT POINTS
# ============================================================

# 1. for loop is best when number of iterations is known
# 2. while loop is best when condition-based repetition needed
# 3. break stops loop completely
# 4. continue skips one iteration
# 5. else runs only if loop ends normally

# ============================================================
# End of File: 010 Loops.py
# ============================================================
