# ============================================================
#                    DATA TYPES IN PYTHON
# ============================================================

# Data type defines:
# - What type of value a variable can store
# - How much memory is allocated
# - What operations can be performed on the value

# Python is a dynamically typed language
# → No need to declare data type explicitly

# ============================================================
#                   DATA TYPES SUMMARY TABLE
# ============================================================

# +------------------+------------+-------------------------+------------------+
# | Data Type        | Keyword    | Description             | Mutable         |
# +------------------+------------+-------------------------+------------------+
# | Integer          | int        | Whole numbers           | ❌ No            |
# | Float            | float      | Decimal numbers         | ❌ No            |
# | Complex          | complex    | Real + Imaginary        | ❌ No            |
# | String           | str        | Text data               | ❌ No            |
# | Boolean          | bool       | True / False            | ❌ No            |
# | List             | list       | Ordered collection      | ✅ Yes           |
# | Tuple            | tuple      | Ordered, fixed          | ❌ No            |
# | Set              | set        | Unordered, unique       | ✅ Yes           |
# | Dictionary       | dict       | Key-value pairs         | ✅ Yes           |
# +------------------+------------+-------------------------+------------------+

# ============================================================
#               1. INTEGER DATA TYPE (int)
# ============================================================

# Stores whole numbers (positive, negative, zero)
# No size limit in Python (depends on memory)

x = 10
y = -50
z = 0

print(x, y, z)
print(type(x))

# ============================================================
#               2. FLOAT DATA TYPE (float)
# ============================================================

# Stores decimal values
# Used in calculations involving fractions

price = 99.99
temperature = -10.5

print(price)
print(type(price))

# ============================================================
#               3. COMPLEX DATA TYPE (complex)
# ============================================================

# Used in mathematical and scientific calculations
# Format → real + imaginary (j)

num = 3 + 4j

print(num)
print(type(num))
print(num.real)      # Real part
print(num.imag)      # Imaginary part

# ============================================================
#               4. STRING DATA TYPE (str)
# ============================================================

# Stores text data
# Strings are immutable

name = "Ethical Hacker"
course = 'Python Programming'

print(name)
print(type(name))

# String indexing
print(name[0])       # First character
print(name[-1])      # Last character

# String slicing
print(name[0:7])

# ============================================================
#               5. BOOLEAN DATA TYPE (bool)
# ============================================================

# Stores True or False
# Mostly used in conditions

is_logged_in = True
is_admin = False

print(is_logged_in)
print(type(is_logged_in))

# ============================================================
#               6. LIST DATA TYPE (list)
# ============================================================

# Ordered and mutable collection
# Allows duplicate values
# Can store different data types

numbers = [1, 2, 3, 4, 5]
mixed_data = [10, "Python", 3.14, True]

print(numbers)
print(type(numbers))

# Accessing list elements
print(numbers[0])

# Modifying list
numbers[1] = 20
print(numbers)

# ============================================================
#               7. TUPLE DATA TYPE (tuple)
# ============================================================

# Ordered and immutable collection
# Faster than list
# Used when data should not change

colors = ("red", "green", "blue")

print(colors)
print(type(colors))

# Accessing tuple elements
print(colors[1])

# ============================================================
#               8. SET DATA TYPE (set)
# ============================================================

# Unordered collection
# Stores unique elements only
# No indexing allowed

unique_numbers = {1, 2, 3, 3, 4, 5}

print(unique_numbers)
print(type(unique_numbers))

# Adding element to set
unique_numbers.add(10)
print(unique_numbers)

# ============================================================
#               9. DICTIONARY DATA TYPE (dict)
# ============================================================

# Stores data in key : value pairs
# Keys must be unique and immutable

student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}

print(student)
print(type(student))

# Accessing dictionary values
print(student["name"])

# Modifying dictionary
student["age"] = 22
print(student)

# ============================================================
#               TYPE CHECKING & CONVERSION
# ============================================================

a = 10
b = float(a)
c = str(a)

print(b, type(b))
print(c, type(c))

# ============================================================
# End of File: 006 Data_Types.py
# ============================================================
