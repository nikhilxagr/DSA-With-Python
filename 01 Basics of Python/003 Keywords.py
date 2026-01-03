# ============================================================
#                     PYTHON KEYWORDS
# ============================================================

# +--------------------+--------------------------------------+
# | Term               | Description                          |
# +--------------------+--------------------------------------+
# | Keyword            | Reserved words in Python             |
# +--------------------+--------------------------------------+
# | Purpose            | Used to define syntax & structure    |
# +--------------------+--------------------------------------+
# | Case Sensitivity   | Keywords are lowercase only          |
# +--------------------+--------------------------------------+
# | Variable Usage     | Cannot be used as variable names     |
# +--------------------+--------------------------------------+

# ============================================================
#               LIST OF PYTHON KEYWORDS (Python 3)
# ============================================================

# False     await     else      import     pass
# None      break     except    in         raise
# True      class     finally   is         return
# and       continue  for       lambda    try
# as        def       from      nonlocal  while
# assert    del       global    not       with
# async     elif      if        or        yield

# ============================================================
#               IMPORTANT RULES
# ============================================================

# 1. Keywords cannot be used as identifiers
# 2. Keywords have predefined meaning
# 3. Keywords are always written in lowercase
# 4. Total number of keywords may change with Python version

# ============================================================
#               SAMPLE CODE (VALID USAGE)
# ============================================================

# Using keyword 'if'
age = 18

if age >= 18:
    print("You are eligible to vote")

# Using keyword 'for'
for i in range(3):
    print(i)

# Using keyword 'def'
def greet():
    return "Hello Python"

print(greet())

# ============================================================
#               INVALID USAGE (DO NOT UNCOMMENT)
# ============================================================

# if = 10        # ❌ Invalid: 'if' is a keyword
# for = 5       # ❌ Invalid: 'for' is a keyword
# class = "A"   # ❌ Invalid: 'class' is a keyword

# ============================================================
# End of File: 003 Keywords.py
# ============================================================
