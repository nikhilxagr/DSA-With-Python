# ============================================================
#              PYTHON STANDARD LIBRARY (PSL)
# ============================================================

# Python Standard Library is a collection of built-in modules
# that come pre-installed with Python.
# No need to install them separately.

# It helps to:
# 1. Reduce code length
# 2. Avoid reinventing the wheel
# 3. Build powerful applications faster

# ============================================================
#          PYTHON STANDARD LIBRARY SUMMARY TABLE
# ============================================================

# +--------------------+--------------------------------------+
# | Module             | Purpose                              |
# +--------------------+--------------------------------------+
# | math               | Mathematical operations              |
# | random             | Random number generation             |
# | datetime           | Date and time handling               |
# | os                 | Operating system interaction         |
# | sys                | Python runtime info                  |
# | time               | Time-related functions               |
# | calendar           | Calendar operations                  |
# | json               | JSON data handling                   |
# | statistics         | Statistical operations               |
# | collections        | Specialized data structures          |
# +--------------------+--------------------------------------+

# ============================================================
#               1. math MODULE
# ============================================================

import math

print(math.sqrt(25))
print(math.factorial(5))
print(math.pow(2, 3))
print(math.pi)
print(math.ceil(4.3))
print(math.floor(4.9))

# ============================================================
#               2. random MODULE
# ============================================================

import random

print(random.randint(1, 10))        # Random integer
print(random.random())              # Random float (0-1)
print(random.choice([1, 2, 3, 4]))  # Random choice from list

items = [10, 20, 30, 40]
random.shuffle(items)
print(items)

# ============================================================
#               3. datetime MODULE
# ============================================================

import datetime

now = datetime.datetime.now()
print("Current Date & Time:", now)

today = datetime.date.today()
print("Today:", today)

# Custom date
custom_date = datetime.date(2025, 1, 1)
print(custom_date)

# ============================================================
#               4. time MODULE
# ============================================================

import time

print("Start")
time.sleep(1)   # Pause execution for 1 second
print("End")

print("Current Time (Epoch):", time.time())

# ============================================================
#               5. os MODULE
# ============================================================

import os

print("Current Working Directory:", os.getcwd())
print("Files in directory:", os.listdir())

# Create folder (safe check)
if not os.path.exists("test_folder"):
    os.mkdir("test_folder")

# ============================================================
#               6. sys MODULE
# ============================================================

import sys

print("Python Version:", sys.version)
print("Command Line Arguments:", sys.argv)
print("Module Search Path:", sys.path)

# ============================================================
#               7. calendar MODULE
# ============================================================

import calendar

print(calendar.month(2025, 1))
print(calendar.isleap(2024))

# ============================================================
#               8. json MODULE
# ============================================================

import json

# Python dictionary
data = {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}

# Convert dict → JSON string
json_data = json.dumps(data)
print(json_data)

# Convert JSON string → dict
python_data = json.loads(json_data)
print(python_data)

# ============================================================
#               9. statistics MODULE
# ============================================================

import statistics

numbers = [10, 20, 30, 40, 50]

print("Mean:", statistics.mean(numbers))
print("Median:", statistics.median(numbers))
print("Mode:", statistics.mode(numbers))

# ============================================================
#               10. collections MODULE
# ============================================================

from collections import Counter, deque, namedtuple

# Counter
words = ["python", "java", "python", "c", "java", "python"]
count = Counter(words)
print(count)

# deque
dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
print(dq)

# namedtuple
Student = namedtuple("Student", ["name", "age"])
s = Student("Rahul", 21)
print(s.name, s.age)

# ============================================================
#               REAL-LIFE EXAMPLES
# ============================================================

# ------------------------------------------------------------
# Example 1: Random password generator
# ------------------------------------------------------------

import string
import random

chars = string.ascii_letters + string.digits
password = "".join(random.choice(chars) for _ in range(8))
print("Generated Password:", password)

# ------------------------------------------------------------
# Example 2: Log current time into file
# ------------------------------------------------------------

from datetime import datetime

with open("system_log.txt", "a") as file:
    file.write(f"Program run at: {datetime.now()}\n")

# ------------------------------------------------------------
# Example 3: Count word frequency
# ------------------------------------------------------------

text = "python is easy and python is powerful"
word_count = Counter(text.split())
print(word_count)

# ============================================================
#               COMMON MISTAKES
# ============================================================

# 1. Importing unnecessary modules
# 2. Using time.sleep() excessively
# 3. Forgetting to close files
# 4. Rewriting functionality already in PSL

# ============================================================
#               IMPORTANT POINTS
# ============================================================

# 1. Python Standard Library comes pre-installed
# 2. Always check documentation for modules
# 3. Use PSL to write efficient code
# 4. Helps in interviews & real-world projects
# 5. Reduces dependency on third-party libraries

# ============================================================
# End of File: 020 Python_Standard_Library.py
# ============================================================
