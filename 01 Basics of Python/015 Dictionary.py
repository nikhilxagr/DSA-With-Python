# ============================================================
#                    DICTIONARY IN PYTHON
# ============================================================

# A dictionary is a collection of data stored as
# key : value pairs
# Dictionaries are MUTABLE and UNORDERED (before Python 3.7)
# From Python 3.7+, dictionaries maintain insertion order

# ============================================================
#               DICTIONARY SUMMARY TABLE
# ============================================================

# +--------------------+--------------------------------------+
# | Feature            | Description                          |
# +--------------------+--------------------------------------+
# | Data Structure     | Key : Value pairs                    |
# | Mutable            | Yes                                  |
# | Keys               | Unique & Immutable                   |
# | Values             | Can be duplicate & mutable           |
# | Indexing           | Not supported                        |
# | Syntax             | {}                                   |
# +--------------------+--------------------------------------+

# ============================================================
#               DICTIONARY CREATION
# ============================================================

student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python",
    "is_active": True
}

print(student)
print(type(student))

# Empty dictionary
empty_dict = {}
print(type(empty_dict))

# ============================================================
#               ACCESSING VALUES
# ============================================================

print(student["name"])      # Access using key
print(student.get("age"))  # Using get() method

# get() avoids error if key not found
print(student.get("marks"))        # None
print(student.get("marks", 0))     # Default value

# ============================================================
#               ADDING & UPDATING VALUES
# ============================================================

# Add new key-value pair
student["marks"] = 85
print(student)

# Update existing value
student["age"] = 22
print(student)

# ============================================================
#               REMOVING ITEMS
# ============================================================

# pop() → removes specific key
student.pop("is_active")
print(student)

# popitem() → removes last inserted item
student.popitem()
print(student)

# del → delete key
del student["age"]
print(student)

# clear() → removes all items
student.clear()
print(student)

# ============================================================
#               DICTIONARY METHODS
# ============================================================

info = {
    "name": "Aman",
    "age": 23,
    "course": "Java"
}

print(info.keys())     # All keys
print(info.values())   # All values
print(info.items())    # Key-value pairs

# ============================================================
#               LOOPING THROUGH DICTIONARY
# ============================================================

# Loop through keys
for key in info:
    print(key, ":", info[key])

# Loop through values
for value in info.values():
    print(value)

# Loop through key-value pairs
for key, value in info.items():
    print(key, "=>", value)

# ============================================================
#               CHECKING KEY EXISTENCE
# ============================================================

print("name" in info)
print("salary" not in info)

# ============================================================
#               NESTED DICTIONARY
# ============================================================

students = {
    "student1": {
        "name": "Rahul",
        "age": 21
    },
    "student2": {
        "name": "Aman",
        "age": 22
    }
}

print(students)
print(students["student1"]["name"])

# ============================================================
#               DICTIONARY COMPREHENSION
# ============================================================

# Create dictionary of squares
squares = {x: x * x for x in range(1, 6)}
print(squares)

# With condition
even_squares = {x: x * x for x in range(1, 11) if x % 2 == 0}
print(even_squares)

# ============================================================
#               COPYING DICTIONARY
# ============================================================

original = {"a": 1, "b": 2}
copy_dict = original.copy()

copy_dict["c"] = 3

print("Original:", original)
print("Copy:", copy_dict)

# ============================================================
#               FROMKEYS METHOD
# ============================================================

keys = ["name", "age", "course"]
default_dict = dict.fromkeys(keys, None)

print(default_dict)

# ============================================================
#               REAL-LIFE EXAMPLES
# ============================================================

# ------------------------------------------------------------
# Example 1: Student record system
# ------------------------------------------------------------

student = {
    "name": "Rahul",
    "marks": [80, 85, 90]
}

total = sum(student["marks"])
percentage = total / len(student["marks"])

print("Total:", total)
print("Percentage:", percentage)

# ------------------------------------------------------------
# Example 2: Word frequency counter
# ------------------------------------------------------------

sentence = "python is easy and python is powerful"
words = sentence.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)

# ------------------------------------------------------------
# Example 3: Simple login system
# ------------------------------------------------------------

users = {
    "admin": "1234",
    "user": "abcd"
}

username = input("Enter username: ")
password = input("Enter password: ")

if users.get(username) == password:
    print("Login successful")
else:
    print("Invalid credentials")

# ============================================================
#               COMMON MISTAKES
# ============================================================

# 1. Using mutable types as keys (❌ list, set)
# 2. Accessing key directly without checking existence
# 3. Confusing dict with list indexing

# ============================================================
#               IMPORTANT POINTS
# ============================================================

# 1. Keys must be unique & immutable
# 2. Values can be anything
# 3. Dictionaries are very fast (hash-based)
# 4. Use get() to avoid KeyError
# 5. Dictionary comprehension is powerful

# ============================================================
# End of File: 015 Dictionary.py
# ============================================================
