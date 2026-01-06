# ============================================================
#               MODULES AND PACKAGES IN PYTHON
# ============================================================

# A MODULE is a file that contains Python code
# A PACKAGE is a collection of modules organized in folders

# Using modules & packages helps in:
# 1. Code reusability
# 2. Better project structure
# 3. Easy maintenance
# 4. Team collaboration

# ============================================================
#               MODULES vs PACKAGES SUMMARY TABLE
# ============================================================

# +--------------------+------------------------+--------------------+
# | Feature            | Module                 | Package            |
# +--------------------+------------------------+--------------------+
# | Definition         | Single .py file        | Folder of modules  |
# | Purpose            | Organize code          | Organize modules   |
# | File Type          | .py                    | Folder             |
# | __init__.py        | Not required           | Required (older)   |
# | Example            | math.py                | numpy, pandas      |
# +--------------------+------------------------+--------------------+

# ============================================================
#               1. USING BUILT-IN MODULES
# ============================================================

# Python comes with many built-in modules

import math

print(math.sqrt(16))
print(math.factorial(5))
print(math.pi)

# ============================================================
#               IMPORTING SPECIFIC FUNCTIONS
# ============================================================

from math import sqrt, pow

print(sqrt(25))
print(pow(2, 3))

# ============================================================
#               USING ALIAS (as)
# ============================================================

import math as m

print(m.sqrt(36))
print(m.pi)

# ============================================================
#               IMPORT EVERYTHING (NOT RECOMMENDED)
# ============================================================

# from math import *
# print(sqrt(49))

# ❌ Avoid this in real projects (causes confusion)

# ============================================================
#               2. CREATING YOUR OWN MODULE
# ============================================================

# Step 1: Create a file named mymodule.py
# Step 2: Write code inside it

# ---- mymodule.py ----
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Step 3: Import and use the module

# import mymodule
# print(mymodule.add(10, 5))
# print(mymodule.subtract(10, 5))

# ============================================================
#               3. __name__ == "__main__"
# ============================================================

# Used to check whether a file is run directly
# or imported as a module

def main():
    print("This file is running directly")

if __name__ == "__main__":
    main()

# ============================================================
#               4. PACKAGES IN PYTHON
# ============================================================

# A package is a directory containing multiple modules

# Example structure:
#
# mypackage/
# ├── __init__.py
# ├── math_utils.py
# └── string_utils.py

# ---- math_utils.py ----
def add(a, b):
    return a + b

# ---- string_utils.py ----
def upper(text):
    return text.upper()

# ============================================================
#               IMPORTING FROM PACKAGES
# ============================================================

# from mypackage import math_utils
# print(math_utils.add(5, 3))

# from mypackage.string_utils import upper
# print(upper("python"))

# ============================================================
#               5. BUILT-IN USEFUL MODULES
# ============================================================

import random
import datetime
import os

# random module
print(random.randint(1, 10))

# datetime module
now = datetime.datetime.now()
print(now)

# os module
print(os.getcwd())

# ============================================================
#               6. sys MODULE
# ============================================================

import sys

print(sys.version)
print(sys.path)

# ============================================================
#               REAL-LIFE EXAMPLES
# ============================================================

# ------------------------------------------------------------
# Example 1: Random OTP generator
# ------------------------------------------------------------

import random

otp = random.randint(100000, 999999)
print("Your OTP:", otp)

# ------------------------------------------------------------
# Example 2: Log current date & time
# ------------------------------------------------------------

from datetime import datetime

with open("log.txt", "a") as file:
    file.write(f"Login time: {datetime.now()}\n")

# ------------------------------------------------------------
# Example 3: File existence checker
# ------------------------------------------------------------

import os

filename = "data.txt"

if os.path.exists(filename):
    print("File exists")
else:
    print("File not found")

# ============================================================
#               COMMON MISTAKES
# ============================================================

# 1. Wrong module name spelling
# 2. Circular imports
# 3. Using import * unnecessarily
# 4. Forgetting __init__.py in old Python versions

# ============================================================
#               IMPORTANT POINTS
# ============================================================

# 1. Use modules to split code logically
# 2. Use packages for large projects
# 3. Use aliases for readability
# 4. __name__ == "__main__" is very important
# 5. Prefer explicit imports

# ============================================================
# End of File: 019 Modules_Packages.py
# ============================================================
