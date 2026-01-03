# ============================================================
#                    OPERATORS IN PYTHON
# ============================================================

# +----------------------+------------------------------------+
# | Operator             | Description                        |
# +----------------------+------------------------------------+
# | Arithmetic           | Perform mathematical operations    |
# | Comparison           | Compare two values                 |
# | Assignment           | Assign values to variables         |
# | Logical              | Perform logical operations         |
# | Bitwise              | Perform bit-level operations       |
# | Membership           | Test membership in sequence        |
# | Identity             | Compare memory locations           |
# +----------------------+------------------------------------+

# ============================================================
#               1. ARITHMETIC OPERATORS
# ============================================================

a = 10
b = 3

print(a + b)   # Addition → 13
print(a - b)   # Subtraction → 7
print(a * b)   # Multiplication → 30
print(a / b)   # Division → 3.333...
print(a % b)   # Modulus → 1
print(a ** b)  # Exponent → 1000
print(a // b)  # Floor Division → 3

# ============================================================
#               2. COMPARISON OPERATORS
# ============================================================

x = 5
y = 10

print(x == y)  # Equal → False
print(x != y)  # Not Equal → True
print(x > y)   # Greater than → False
print(x < y)   # Less than → True
print(x >= y)  # Greater than or equal → False
print(x <= y)  # Less than or equal → True

# ============================================================
#               3. ASSIGNMENT OPERATORS
# ============================================================

num = 10

num += 5   # num = num + 5 → 15
num -= 2   # num = num - 2 → 13
num *= 2   # num = num * 2 → 26
num /= 2   # num = num / 2 → 13.0
num %= 3   # num = num % 3 → 1

print(num)

# ============================================================
#               4. LOGICAL OPERATORS
# ============================================================

p = True
q = False

print(p and q)  # AND → False
print(p or q)   # OR → True
print(not p)    # NOT → False

# ============================================================
#               5. BITWISE OPERATORS
# ============================================================

m = 5    # 101
n = 3    # 011

print(m & n)   # AND → 1
print(m | n)   # OR → 7
print(m ^ n)   # XOR → 6
print(~m)      # NOT → -6
print(m << 1)  # Left shift → 10
print(m >> 1)  # Right shift → 2

# ============================================================
#               6. MEMBERSHIP OPERATORS
# ============================================================

text = "python"

print('p' in text)      # True
print('z' not in text)  # True

# ============================================================
#               7. IDENTITY OPERATORS
# ============================================================

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)       # True
print(a is c)       # False
print(a is not c)   # True

# ============================================================
# End of File: Operators.py
# ============================================================
