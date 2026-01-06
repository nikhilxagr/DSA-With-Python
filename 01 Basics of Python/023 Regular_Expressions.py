# ============================================================
#               REGULAR EXPRESSIONS (REGEX) IN PYTHON
# ============================================================

# Regular Expressions are used to:
# - Search text
# - Match patterns
# - Validate data
# - Extract information from strings

# Python provides the built-in 're' module for regex operations

# ============================================================
#               REGEX SUMMARY TABLE
# ============================================================

# +--------------------+--------------------------------------+
# | Term               | Description                          |
# +--------------------+--------------------------------------+
# | Regex              | Pattern for matching text            |
# | re module          | Python regex library                 |
# | Pattern            | Rules to match strings               |
# | Match              | Found pattern in text                |
# | Flags              | Modify regex behavior                |
# +--------------------+--------------------------------------+

# ============================================================
#               IMPORT REGEX MODULE
# ============================================================

import re

# ============================================================
#               BASIC REGEX FUNCTIONS
# ============================================================

# +----------------+------------------------------------------+
# | Function       | Purpose                                  |
# +----------------+------------------------------------------+
# | re.search()    | Search pattern anywhere in string        |
# | re.match()     | Match pattern at beginning               |
# | re.findall()   | Return all matches as list               |
# | re.sub()       | Replace matched text                    |
# | re.split()     | Split string using regex                |
# +----------------+------------------------------------------+

# ============================================================
#               1. re.search()
# ============================================================

text = "Python is easy and powerful"

result = re.search("easy", text)

if result:
    print("Found:", result.group())
else:
    print("Not found")

# ============================================================
#               2. re.match()
# ============================================================

result = re.match("Python", text)
print(result.group() if result else "No match")

# ============================================================
#               3. re.findall()
# ============================================================

text = "Python Java C Python Java"

languages = re.findall("Python", text)
print(languages)

# ============================================================
#               4. re.sub()
# ============================================================

text = "I love Java"
new_text = re.sub("Java", "Python", text)
print(new_text)

# ============================================================
#               5. re.split()
# ============================================================

data = "apple,banana;orange mango"
result = re.split("[,; ]", data)
print(result)

# ============================================================
#               REGEX METACHARACTERS
# ============================================================

# +------------+----------------------------------------------+
# | Symbol     | Meaning                                      |
# +------------+----------------------------------------------+
# | .          | Any character except newline                |
# | ^          | Start of string                              |
# | $          | End of string                                |
# | *          | 0 or more occurrences                       |
# | +          | 1 or more occurrences                       |
# | ?          | 0 or 1 occurrence                           |
# | []         | Character set                               |
# | |          | OR                                          |
# | ()         | Grouping                                    |
# | {}         | Exact repetitions                           |
# +------------+----------------------------------------------+

# ============================================================
#               CHARACTER CLASSES
# ============================================================

# +------------+----------------------------------------------+
# | Pattern    | Meaning                                      |
# +------------+----------------------------------------------+
# | \d         | Digit (0–9)                                  |
# | \D         | Non-digit                                   |
# | \w         | Alphanumeric (a-z, A-Z, 0-9, _)             |
# | \W         | Non-alphanumeric                            |
# | \s         | Whitespace                                  |
# | \S         | Non-whitespace                              |
# +------------+----------------------------------------------+

# Example
text = "User123"
print(re.findall(r"\d+", text))   # Digits
print(re.findall(r"\w+", text))   # Words

# ============================================================
#               QUANTIFIERS
# ============================================================

# a*   → 0 or more
# a+   → 1 or more
# a?   → 0 or 1
# a{2} → exactly 2
# a{2,4} → between 2 and 4

text = "aaabbbcccc"
print(re.findall(r"a+", text))
print(re.findall(r"b{3}", text))

# ============================================================
#               REGEX FLAGS
# ============================================================

# +----------------+------------------------------------------+
# | Flag           | Purpose                                  |
# +----------------+------------------------------------------+
# | re.I           | Ignore case                              |
# | re.M           | Multiline                                |
# | re.S           | Dot matches newline                     |
# | re.X           | Verbose regex                           |
# +----------------+------------------------------------------+

text = "python PYTHON PyThOn"
print(re.findall("python", text, re.I))

# ============================================================
#               GROUPING & CAPTURING
# ============================================================

text = "My email is test@gmail.com"

match = re.search(r"(\w+)@(\w+)\.(\w+)", text)

if match:
    print(match.group())     # Full match
    print(match.group(1))    # Username
    print(match.group(2))    # Domain
    print(match.group(3))    # Extension

# ============================================================
#               REAL-LIFE REGEX EXAMPLES
# ============================================================

# ------------------------------------------------------------
# Example 1: Email validation
# ------------------------------------------------------------

email = "user123@gmail.com"
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")

# ------------------------------------------------------------
# Example 2: Phone number validation (India)
# ------------------------------------------------------------

phone = "9876543210"
pattern = r"^[6-9]\d{9}$"

print("Valid phone" if re.match(pattern, phone) else "Invalid phone")

# ------------------------------------------------------------
# Example 3: Password validation
# ------------------------------------------------------------

password = "Python@123"
pattern = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&]).{8,}$"

print("Strong password" if re.match(pattern, password) else "Weak password")

# ------------------------------------------------------------
# Example 4: Extract all numbers from text
# ------------------------------------------------------------

text = "Order 3 items for 250 rupees on 12th"
numbers = re.findall(r"\d+", text)
print(numbers)

# ------------------------------------------------------------
# Example 5: URL validation
# ------------------------------------------------------------

url = "https://www.example.com"
pattern = r"^(https?|ftp)://[^\s/$.?#].[^\s]*$"

print("Valid URL" if re.match(pattern, url) else "Invalid URL")

# ============================================================
#               COMMON MISTAKES
# ============================================================

# 1. Forgetting raw string (r"pattern")
# 2. Overusing .* (can cause performance issues)
# 3. Not anchoring pattern with ^ and $
# 4. Making regex too complex unnecessarily

# ============================================================
#               IMPORTANT POINTS
# ============================================================

# 1. Regex is powerful but should be readable
# 2. Always test regex patterns
# 3. Use raw strings (r"") for regex
# 4. Prefer simple patterns
# 5. Regex is heavily used in cybersecurity, validation, parsing

# ============================================================
# End of File: 023 Regular_Expressions.py
# ============================================================
