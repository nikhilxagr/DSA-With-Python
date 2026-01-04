# ============================================================
#              INPUT AND OUTPUT IN PYTHON
# ============================================================

# Input  → Used to take data from the user
# Output → Used to display data to the user

# Python uses:
# input()  → for input
# print()  → for output

# ============================================================
#               INPUT & OUTPUT SUMMARY TABLE
# ============================================================

# +----------------+------------------------------------------+
# | Function       | Description                              |
# +----------------+------------------------------------------+
# | input()        | Takes input from user (as string)        |
# | print()        | Displays output on screen                |
# | type()         | Shows data type of variable              |
# +----------------+------------------------------------------+

# ============================================================
#               BASIC OUTPUT USING print()
# ============================================================

print("Hello, Python")
print(10)
print(3.14)
print(True)

# Printing multiple values
print("Age:", 21)
print("Python", "is", "easy")

# ============================================================
#               BASIC INPUT USING input()
# ============================================================

# input() always returns STRING data

name = input("Enter your name: ")
print("Your name is:", name)
print(type(name))   # Always <class 'str'>

# ============================================================
#               INPUT WITH TYPE CASTING
# ============================================================

# Taking integer input
age = int(input("Enter your age: "))
print("Age:", age)
print(type(age))

# Taking float input
price = float(input("Enter price: "))
print("Price:", price)
print(type(price))

# ============================================================
#               MULTIPLE INPUTS
# ============================================================

# Method 1: Using multiple input statements
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)

# Method 2: Using split()
x, y = input("Enter two numbers separated by space: ").split()
x = int(x)
y = int(y)

print("Product:", x * y)

# ============================================================
#               OUTPUT FORMATTING
# ============================================================

# Method 1: Comma separated (default)
name = "Rahul"
age = 21
print(name, age)

# Method 2: Using + operator (string concatenation)
print("Name: " + name + ", Age: " + str(age))

# Method 3: Using f-strings (BEST & MODERN)
print(f"Name: {name}, Age: {age}")

# ============================================================
#               print() PARAMETERS
# ============================================================

# sep → Separator between values
print("Python", "Java", "C++", sep=" | ")

# end → What to print at end
print("Hello", end=" ")
print("World")

# ============================================================
#               INPUT + OUTPUT REAL LIFE EXAMPLE
# ============================================================

# Program to calculate total marks and percentage

math = int(input("Enter Math marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

total = math + science + english
percentage = total / 3

print("Total Marks:", total)
print("Percentage:", percentage)

# Using formatted output
print(f"Total = {total}, Percentage = {percentage:.2f}%")

# ============================================================
#               COMMON MISTAKES (DO NOT UNCOMMENT)
# ============================================================

# age = input("Enter age: ")
# print(age + 5)   # ❌ Error: cannot add string and int

# ============================================================
#               IMPORTANT POINTS
# ============================================================

# 1. input() always returns string
# 2. Use type casting to convert input
# 3. f-strings are fastest and cleanest
# 4. print() supports sep and end parameters

# ============================================================
# End of File: 008 Input_Output.py
# ============================================================
