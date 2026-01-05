# ============================================================
#                       LISTS IN PYTHON
# ============================================================

# A list is an ordered collection of items
# Lists are MUTABLE (can be changed after creation)
# Lists can store multiple data types

# ============================================================
#                   LISTS SUMMARY TABLE
# ============================================================

# +--------------------+--------------------------------------+
# | Feature            | Description                          |
# +--------------------+--------------------------------------+
# | Ordered            | Elements have fixed order            |
# | Mutable            | Elements can be modified             |
# | Indexing           | Supports positive & negative index   |
# | Duplicates         | Allows duplicate values              |
# | Mixed Data Types   | Can store different data types       |
# +--------------------+--------------------------------------+

# ============================================================
#               LIST CREATION
# ============================================================

numbers = [1, 2, 3, 4, 5]
names = ["Python", "Java", "C++"]
mixed = [10, "Python", 3.14, True]

print(numbers)
print(names)
print(mixed)
print(type(numbers))

# ============================================================
#               LIST INDEXING
# ============================================================

langs = ["Python", "Java", "C++", "JavaScript"]

print(langs[0])    # First element
print(langs[1])
print(langs[-1])   # Last element
print(langs[-2])

# ============================================================
#               LIST SLICING
# ============================================================

# Syntax: list[start : end : step]

print(langs[0:2])     # ['Python', 'Java']
print(langs[1:])      # ['Java', 'C++', 'JavaScript']
print(langs[:3])      # ['Python', 'Java', 'C++']
print(langs[::-1])    # Reverse list

# ============================================================
#               LIST MUTABILITY
# ============================================================

nums = [10, 20, 30]
nums[1] = 99   # Modify element
print(nums)

# ============================================================
#               ADDING ELEMENTS TO LIST
# ============================================================

data = [1, 2, 3]

data.append(4)        # Add at end
print(data)

data.insert(1, 100)   # Insert at index
print(data)

data.extend([5, 6])   # Add multiple elements
print(data)

# ============================================================
#               REMOVING ELEMENTS FROM LIST
# ============================================================

items = [10, 20, 30, 40, 50]

items.remove(30)   # Remove by value
print(items)

items.pop()        # Remove last element
print(items)

items.pop(1)       # Remove by index
print(items)

del items[0]       # Delete by index
print(items)

# ============================================================
#               LIST METHODS
# ============================================================

nums = [5, 2, 9, 1, 5]

print(nums.count(5))   # Count occurrences
print(nums.index(9))   # Find index

nums.sort()            # Sort ascending
print(nums)

nums.reverse()         # Reverse list
print(nums)

# ============================================================
#               COPY LIST
# ============================================================

a = [1, 2, 3]
b = a.copy()

b.append(4)

print("a:", a)
print("b:", b)

# ============================================================
#               LIST CONCATENATION & REPETITION
# ============================================================

list1 = [1, 2]
list2 = [3, 4]

print(list1 + list2)   # Concatenation
print(list1 * 3)       # Repetition

# ============================================================
#               MEMBERSHIP OPERATORS
# ============================================================

colors = ["red", "green", "blue"]

print("red" in colors)
print("black" not in colors)

# ============================================================
#               LOOPING THROUGH LIST
# ============================================================

for color in colors:
    print(color)

# Using index
for i in range(len(colors)):
    print(i, colors[i])

# ============================================================
#               LIST COMPREHENSION
# ============================================================

# Create list of squares
squares = [x * x for x in range(1, 6)]
print(squares)

# With condition
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)

# ============================================================
#               NESTED LIST
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
print(matrix[0])
print(matrix[1][2])   # Access nested element

# ============================================================
#               REAL-LIFE EXAMPLES
# ============================================================

# ------------------------------------------------------------
# Example 1: Find largest number
# ------------------------------------------------------------

nums = [10, 45, 23, 89, 12]
largest = nums[0]

for n in nums:
    if n > largest:
        largest = n

print("Largest number:", largest)

# ------------------------------------------------------------
# Example 2: Remove duplicates
# ------------------------------------------------------------

values = [1, 2, 2, 3, 4, 4, 5]
unique = []

for v in values:
    if v not in unique:
        unique.append(v)

print("Unique list:", unique)

# ------------------------------------------------------------
# Example 3: To-do list simulation
# ------------------------------------------------------------

tasks = []

tasks.append("Learn Python")
tasks.append("Practice Lists")
tasks.append("Build Project")

print("Tasks:")
for task in tasks:
    print("-", task)

# ============================================================
#               COMMON MISTAKES
# ============================================================

# 1. Using wrong index → IndexError
# 2. Forgetting list is mutable
# 3. Confusing append() and extend()

# ============================================================
#               IMPORTANT POINTS
# ============================================================

# 1. Lists are mutable
# 2. Indexing starts from 0
# 3. Supports slicing
# 4. List comprehension is powerful & fast
# 5. Use copy() to avoid reference issues

# ============================================================
# End of File: 013 Lists.py
# ============================================================
