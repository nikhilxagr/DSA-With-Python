# ============================================================
#               CONTROL STATEMENTS IN PYTHON
# ============================================================

# Control statements are used to control the flow of execution
# of a program based on conditions or loops.

# Types of Control Statements:
# 1. Conditional Statements
# 2. Looping Statements
# 3. Jump Statements

# ============================================================
#               CONTROL STATEMENTS SUMMARY TABLE
# ============================================================

# +-----------------------+----------------------------------+
# | Type                  | Statements                       |
# +-----------------------+----------------------------------+
# | Conditional           | if, if-else, if-elif-else        |
# | Looping               | for, while                       |
# | Jump                  | break, continue, pass            |
# +-----------------------+----------------------------------+

# ============================================================
#               1. CONDITIONAL STATEMENTS
# ============================================================

# Conditional statements execute code based on a condition

# ============================================================
#               IF STATEMENT
# ============================================================

age = 20

if age >= 18:
    print("You are eligible to vote")

# ============================================================
#               IF - ELSE STATEMENT
# ============================================================

number = 5

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# ============================================================
#               IF - ELIF - ELSE STATEMENT
# ============================================================

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# ============================================================
#               NESTED IF STATEMENT
# ============================================================

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Invalid user")

# ============================================================
#               2. LOOPING STATEMENTS
# ============================================================

# Loops are used to repeat a block of code

# ============================================================
#               FOR LOOP
# ============================================================

# Printing numbers from 1 to 5
for i in range(1, 6):
    print(i)

# Loop through a list
languages = ["Python", "Java", "C++"]

for lang in languages:
    print(lang)

# ============================================================
#               WHILE LOOP
# ============================================================

# Print numbers from 1 to 5
count = 1

while count <= 5:
    print(count)
    count += 1

# ============================================================
#               ELSE WITH LOOPS
# ============================================================

# for-else example
for i in range(3):
    print(i)
else:
    print("Loop completed successfully")

# while-else example
x = 0
while x < 3:
    print(x)
    x += 1
else:
    print("While loop finished")

# ============================================================
#               3. JUMP STATEMENTS
# ============================================================

# Jump statements alter loop execution

# ============================================================
#               BREAK STATEMENT
# ============================================================

for i in range(1, 6):
    if i == 4:
        break
    print(i)

# ============================================================
#               CONTINUE STATEMENT
# ============================================================

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# ============================================================
#               PASS STATEMENT
# ============================================================

# pass is used as a placeholder where statement is required

for i in range(3):
    if i == 1:
        pass
    print(i)

# ============================================================
#               REAL-LIFE EXAMPLE
# ============================================================

# Program to check login attempts

attempts = 3

while attempts > 0:
    pin = input("Enter PIN: ")
    if pin == "1234":
        print("Access Granted")
        break
    else:
        attempts -= 1
        print("Wrong PIN. Attempts left:", attempts)
else:
    print("Account blocked")

# ============================================================
#               IMPORTANT POINTS
# ============================================================

# 1. Indentation is mandatory in Python
# 2. Conditions must return True or False
# 3. break exits the loop completely
# 4. continue skips current iteration
# 5. pass does nothing (placeholder)

# ============================================================
# End of File: 009 Control_Statements.py
# ============================================================
