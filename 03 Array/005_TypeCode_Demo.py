"""
Filename: typecode_demo.py
Description: Demonstrates the concept of typecodes in Python using the array module.
Author: Your Name
Date: YYYY-MM-DD
"""

from array import array

# ----------------------------------------
# What is a Typecode?
# ----------------------------------------
# A typecode is a single character that defines
# the data type of elements stored in an array.
# All elements in an array must be of the same type.

# ----------------------------------------
# Common Typecodes and Their Meanings
# ----------------------------------------
# 'b' -> signed char
# 'B' -> unsigned char
# 'i' -> signed integer
# 'I' -> unsigned integer
# 'f' -> floating point number
# 'd' -> double precision floating point
# 'u' -> unicode character

# ----------------------------------------
# Integer Array Example
# ----------------------------------------
int_array = array('i', [10, 20, 30, 40])
print("Integer Array:", int_array)

# ----------------------------------------
# Floating Point Array Example
# ----------------------------------------
float_array = array('f', [1.5, 2.5, 3.5])
print("Float Array:", float_array)

# ----------------------------------------
# Double Precision Float Array Example
# ----------------------------------------
double_array = array('d', [10.123, 20.456, 30.789])
print("Double Array:", double_array)

# ----------------------------------------
# Unicode Character Array Example
# ----------------------------------------
char_array = array('u', ['A', 'B', 'C'])
print("Character Array:", char_array)

# ----------------------------------------
# Key Notes
# ----------------------------------------
# - Typecodes define memory size and data type
# - Arrays are more memory efficient than lists
# - Arrays allow only one data type

print("\nProgram executed successfully.")
