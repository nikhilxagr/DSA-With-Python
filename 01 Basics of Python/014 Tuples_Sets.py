# ============================================================
#                TUPLES AND SETS IN PYTHON
# ============================================================

# Tuple → Ordered, immutable collection
# Set   → Unordered, mutable collection with unique values

# ============================================================
#               TUPLES vs SETS SUMMARY TABLE
# ============================================================

# +------------------+---------------------+----------------------+
# | Feature          | Tuple               | Set                  |
# +------------------+---------------------+----------------------+
# | Ordered          | Yes                 | No                   |
# | Mutable          | No                  | Yes                  |
# | Indexing         | Yes                 | No                   |
# | Duplicates       | Allowed             | Not Allowed          |
# | Syntax           | ()                  | {}                   |
# | Use Case         | Fixed data          | Unique data          |
# +------------------+---------------------+----------------------+

# ============================================================
#                       TUPLES
# ============================================================

# ============================================================
#               TUPLE CREATION
# ============================================================

t1 = (10, 20, 30)
t2 = ("Python", "Java", "C++")
t3 = (10, "Python", 3.14, True)

print(t1)
print(t2)
print(t3)
print(type(t1))

# Single element tuple (comma is mandatory)
single = (10,)
print(type(single))

# ============================================================
#               TUPLE INDEXING
# ============================================================

langs = ("Python", "Java", "C++", "JavaScript")

print(langs[0])
print(langs[1])
print(langs[-1])

# ============================================================
#               TUPLE SLICING
# ============================================================

print(langs[0:2])
print(langs[1:])
print(langs[::-1])

# ============================================================
#               TUPLE IMMUTABILITY
# ============================================================

# langs[0] = "C"   # ❌ Error: Tuples are immutable

# ============================================================
#               TUPLE METHODS
# ============================================================

nums = (1, 2, 3, 2, 4, 2)

print(nums.count(2))   # Count occurrences
print(nums.index(3))   # Find index

# ============================================================
#               TUPLE UNPACKING
# ============================================================

data = ("Rahul", 21, "Python")

name, age, course = data

print(name)
print(age)
print(course)

# ============================================================
#               NESTED TUPLE
# ============================================================

nested = ((1, 2), (3, 4), (5, 6))

print(nested)
print(nested[1])
print(nested[1][0])

# ============================================================
#               TUPLE USE CASE
# ============================================================

# Tuples are used when data should not change
# Example: Coordinates

coordinates = (10.5, 20.3)
print("X:", coordinates[0], "Y:", coordinates[1])

# ============================================================
#                       SETS
# ============================================================

# ============================================================
#               SET CREATION
# ============================================================

s1 = {1, 2, 3, 4}
s2 = {1, 2, 2, 3, 4, 4}   # Duplicates removed automatically

print(s1)
print(s2)
print(type(s1))

# Empty set (IMPORTANT)
empty_set = set()
print(type(empty_set))

# ============================================================
#               SET PROPERTIES
# ============================================================

# 1. Unordered
# 2. No duplicate values
# 3. No indexing
# 4. Mutable

# ============================================================
#               ADDING ELEMENTS TO SET
# ============================================================

data = {1, 2, 3}

data.add(4)
print(data)

data.update([5, 6, 7])
print(data)

# ============================================================
#               REMOVING ELEMENTS FROM SET
# ============================================================

data.remove(3)     # Error if element not found
print(data)

data.discard(10)   # No error if element not found
print(data)

data.pop()         # Removes random element
print(data)

# ============================================================
#               SET OPERATIONS
# ============================================================

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # Union
print(a & b)   # Intersection
print(a - b)   # Difference
print(a ^ b)   # Symmetric difference

# ============================================================
#               SET METHODS
# ============================================================

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

# ============================================================
#               SET MEMBERSHIP
# ============================================================

colors = {"red", "green", "blue"}

print("red" in colors)
print("black" not in colors)

# ============================================================
#               LOOPING THROUGH SET
# ============================================================

for color in colors:
    print(color)

# ============================================================
#               REAL-LIFE EXAMPLES
# ============================================================

# ------------------------------------------------------------
# Example 1: Remove duplicates using set
# ------------------------------------------------------------

values = [1, 2, 2, 3, 4, 4, 5]
unique_values = set(values)

print("Unique values:", unique_values)

# ------------------------------------------------------------
# Example 2: Common subjects between students
# ------------------------------------------------------------

student1 = {"Math", "Physics", "Python"}
student2 = {"Python", "Java", "Math"}

common_subjects = student1 & student2
print("Common subjects:", common_subjects)

# ------------------------------------------------------------
# Example 3: Tuple + Set combined use
# ------------------------------------------------------------

students = (
    ("Rahul", "Python"),
    ("Aman", "Java"),
    ("Rahul", "Python")
)

unique_students = set(students)
print(unique_students)

# ============================================================
#               COMMON MISTAKES
# ============================================================

# 1. Forgetting comma in single-element tuple
# 2. Using {} for empty set (creates dict)
# 3. Trying to index a set

# ============================================================
#               IMPORTANT POINTS
# ============================================================

# 1. Use tuple for fixed data
# 2. Use set for unique data
# 3. Tuples are faster than lists
# 4. Sets are best for membership testing
# 5. Set operations are very powerful

# ============================================================
# End of File: 014 Tuples_Sets.py
# ============================================================
