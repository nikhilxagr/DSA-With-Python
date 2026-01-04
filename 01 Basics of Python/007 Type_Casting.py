# ============================================================
#                 TYPE CASTING IN PYTHON
# ============================================================

# Type Casting means converting one data type into another.
# Python supports two types of type casting:
# 1. Implicit Type Casting (Automatic)
# 2. Explicit Type Casting (Manual)

# ============================================================
#               TYPE CASTING SUMMARY TABLE
# ============================================================

# +----------------------+------------------------------------+
# | Type Casting         | Description                        |
# +----------------------+------------------------------------+
# | Implicit Casting     | Done automatically by Python       |
# | Explicit Casting     | Done manually by programmer        |
# +----------------------+------------------------------------+

# ============================================================
#               1. IMPLICIT TYPE CASTING
# ============================================================

# Python automatically converts smaller data type
# into larger data type to avoid data loss

a = 10        # int
b = 2.5       # float

result = a + b   # int + float → float

print(result)
print(type(result))   # <class 'float'>

# ============================================================
#               2. EXPLICIT TYPE CASTING
# ============================================================

# Programmer manually converts data types
# using built-in functions

# Common type casting functions:
# int(), float(), str(), bool(), list(), tuple(), set()

# ============================================================
#               INT TYPE CASTING
# ============================================================

x = 10.8
y = int(x)      # float → int (decimal removed)

print(y)
print(type(y))

# String to int
num_str = "25"
num_int = int(num_str)

print(num_int)
print(type(num_int))

# ============================================================
#               FLOAT TYPE CASTING
# ============================================================

a = 10
b = float(a)

print(b)
print(type(b))

# String to float
price_str = "99.99"
price_float = float(price_str)

print(price_float)
print(type(price_float))

# ============================================================
#               STRING TYPE CASTING
# ============================================================

num = 100
text = str(num)

print(text)
print(type(text))

# ============================================================
#               BOOLEAN TYPE CASTING
# ============================================================

print(bool(1))        # True
print(bool(0))        # False
print(bool(""))       # False
print(bool("Python")) # True
print(bool([]))       # False
print(bool([1, 2]))   # True

# ============================================================
#               LIST TYPE CASTING
# ============================================================

# Tuple to list
colors_tuple = ("red", "green", "blue")
colors_list = list(colors_tuple)

print(colors_list)
print(type(colors_list))

# Set to list
numbers_set = {1, 2, 3}
numbers_list = list(numbers_set)

print(numbers_list)

# ============================================================
#               TUPLE TYPE CASTING
# ============================================================

# List to tuple
nums_list = [10, 20, 30]
nums_tuple = tuple(nums_list)

print(nums_tuple)
print(type(nums_tuple))

# ============================================================
#               SET TYPE CASTING
# ============================================================

# List to set (duplicates removed)
values = [1, 2, 2, 3, 4, 4]
unique_values = set(values)

print(unique_values)
print(type(unique_values))

# ============================================================
#               DICTIONARY TYPE CASTING
# ============================================================

# List of tuples to dictionary
data = [("name", "Rahul"), ("age", 21), ("course", "Python")]
student = dict(data)

print(student)
print(type(student))

# ============================================================
#               INVALID TYPE CASTING (DO NOT UNCOMMENT)
# ============================================================

# int("Python")     # ❌ ValueError
# int("10.5")       # ❌ Invalid literal
# list(123)         # ❌ TypeError

# ============================================================
#               REAL-LIFE EXAMPLE
# ============================================================

# User input is always string
user_age = "18"

# Convert string to integer
user_age = int(user_age)

if user_age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# ============================================================
# End of File: 007 Type_Casting.py
# ============================================================
