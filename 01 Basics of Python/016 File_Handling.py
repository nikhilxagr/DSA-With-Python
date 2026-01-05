# ============================================================
#                  FILE HANDLING IN PYTHON
# ============================================================

# File handling allows us to:
# - Create files
# - Read data from files
# - Write data to files
# - Append data to files
# - Delete files

# Python provides built-in functions for file handling

# ============================================================
#               FILE HANDLING SUMMARY TABLE
# ============================================================

# +------------------+----------------------------------------+
# | Mode             | Description                            |
# +------------------+----------------------------------------+
# | 'r'              | Read (default)                         |
# | 'w'              | Write (overwrite if exists)            |
# | 'a'              | Append                                 |
# | 'x'              | Create new file                        |
# | 'rb'             | Read binary file                       |
# | 'wb'             | Write binary file                      |
# +------------------+----------------------------------------+

# ============================================================
#               BASIC FILE OPEN & CLOSE
# ============================================================

# Syntax:
# file = open("filename", "mode")
# file.close()

file = open("sample.txt", "w")
file.write("Hello, this is a sample file.\n")
file.close()

# ============================================================
#               WRITING TO A FILE
# ============================================================

file = open("data.txt", "w")
file.write("Python File Handling\n")
file.write("This will overwrite existing content.\n")
file.close()

# ============================================================
#               READING FROM A FILE
# ============================================================

file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# ============================================================
#               READ LINE BY LINE
# ============================================================

file = open("data.txt", "r")

print(file.readline())  # Read first line
print(file.readline())  # Read second line

file.close()

# ============================================================
#               READ ALL LINES AS LIST
# ============================================================

file = open("data.txt", "r")
lines = file.readlines()
print(lines)
file.close()

# ============================================================
#               APPENDING TO A FILE
# ============================================================

file = open("data.txt", "a")
file.write("This line is appended.\n")
file.close()

# ============================================================
#               USING WITH STATEMENT (BEST PRACTICE)
# ============================================================

# Automatically closes the file

with open("with_example.txt", "w") as file:
    file.write("Using with statement\n")
    file.write("No need to close file manually\n")

with open("with_example.txt", "r") as file:
    print(file.read())

# ============================================================
#               FILE POINTER POSITION
# ============================================================

with open("data.txt", "r") as file:
    print(file.tell())   # Current position
    print(file.read(10)) # Read first 10 characters
    print(file.tell())
    file.seek(0)         # Move pointer to start
    print(file.read())

# ============================================================
#               CHECK IF FILE EXISTS
# ============================================================

import os

print(os.path.exists("data.txt"))
print(os.path.exists("unknown.txt"))

# ============================================================
#               DELETE A FILE
# ============================================================

# WARNING: This permanently deletes the file

# if os.path.exists("delete_me.txt"):
#     os.remove("delete_me.txt")

# ============================================================
#               FILE HANDLING WITH USER INPUT
# ============================================================

filename = input("Enter file name: ")

with open(filename, "w") as file:
    file.write("File created using user input\n")

print("File written successfully")

# ============================================================
#               REAL-LIFE EXAMPLES
# ============================================================

# ------------------------------------------------------------
# Example 1: Student record storage
# ------------------------------------------------------------

with open("students.txt", "a") as file:
    name = input("Enter student name: ")
    marks = input("Enter marks: ")
    file.write(name + " - " + marks + "\n")

# ------------------------------------------------------------
# Example 2: Read student records
# ------------------------------------------------------------

with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())

# ------------------------------------------------------------
# Example 3: Simple log file
# ------------------------------------------------------------

with open("app.log", "a") as log:
    log.write("Application started\n")

# ============================================================
#               COMMON MISTAKES
# ============================================================

# 1. Forgetting to close file
# 2. Using wrong file mode
# 3. Reading file without checking existence
# 4. Overwriting file accidentally using 'w'

# ============================================================
#               IMPORTANT POINTS
# ============================================================

# 1. Always close file or use with statement
# 2. 'w' mode overwrites file content
# 3. 'a' mode preserves existing data
# 4. File paths can be relative or absolute
# 5. Use os module for file operations

# ============================================================
# End of File: 016 File_Handling.py
# ============================================================
