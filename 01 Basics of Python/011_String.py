# ============================================================
#                     STRINGS IN PYTHON
# ============================================================

# A string is a sequence of characters
# Strings are used to store text data
# Strings are IMMUTABLE (cannot be changed after creation)

# ============================================================
#                   STRINGS SUMMARY TABLE
# ============================================================

# +--------------------+--------------------------------------+
# | Concept            | Description                          |
# +--------------------+--------------------------------------+
# | String             | Sequence of characters               |
# | Quotes             | Single (' ') or Double (" ")         |
# | Indexing           | Access characters using index        |
# | Slicing            | Extract part of string               |
# | Immutability       | Cannot modify string directly        |
# | String Methods     | Built-in functions for strings       |
# +--------------------+--------------------------------------+

# ============================================================
#               STRING CREATION
# ============================================================

name1 = "Python"
name2 = 'Programming'
name3 = """This is
a multi-line
string"""

print(name1)
print(name2)
print(name3)

# ============================================================
#               STRING INDEXING
# ============================================================

text = "Python"

# Positive indexing
print(text[0])   # P
print(text[1])   # y

# Negative indexing
print(text[-1])  # n
print(text[-2])  # o

# ============================================================
#               STRING SLICING
# ============================================================

# Syntax: string[start : end : step]

print(text[0:4])     # Pyth
print(text[2:])      # thon
print(text[:3])      # Pyt
print(text[::-1])    # Reverse string

# ============================================================
#               STRING IMMUTABILITY
# ============================================================

# text[0] = 'J'   # ❌ Error: Strings are immutable

# Correct way → create new string
new_text = "J" + text[1:]
print(new_text)

# ============================================================
#               STRING CONCATENATION
# ============================================================

a = "Hello"
b = "World"

print(a + " " + b)

# ============================================================
#               STRING REPETITION
# ============================================================

print("Python " * 3)

# ============================================================
#               STRING LENGTH
# ============================================================

word = "Programming"
print(len(word))

# ============================================================
#               STRING MEMBERSHIP
# ============================================================

print("Py" in "Python")
print("Java" not in "Python")

# ============================================================
#               COMMON STRING METHODS
# ============================================================

msg = "  python programming  "

print(msg.upper())        # Convert to uppercase
print(msg.lower())        # Convert to lowercase
print(msg.title())        # Title case
print(msg.capitalize())  # Capitalize first letter
print(msg.strip())        # Remove spaces
print(msg.replace("python", "java"))
print(msg.find("programming"))
print(msg.count("p"))

# ============================================================
#               STRING CHECK METHODS
# ============================================================

data = "Python123"

print(data.isalpha())     # False
print(data.isdigit())     # False
print(data.isalnum())     # True
print("123".isdigit())    # True
print("Python".isalpha()) # True

# ============================================================
#               SPLIT AND JOIN
# ============================================================

sentence = "Python is very easy"

words = sentence.split()
print(words)

joined = "-".join(words)
print(joined)

# ============================================================
#               STRING FORMATTING
# ============================================================

name = "Rahul"
age = 21

# Method 1: Using commas
print("Name:", name, "Age:", age)

# Method 2: Using format()
print("Name: {}, Age: {}".format(name, age))

# Method 3: Using f-strings (BEST)
print(f"Name: {name}, Age: {age}")

# ============================================================
#               ESCAPE CHARACTERS
# ============================================================

print("Hello\nWorld")   # New line
print("Hello\tWorld")   # Tab space
print("She said \"Hi\"")

# ============================================================
#               STRING COMPARISON
# ============================================================

print("apple" == "apple")
print("Apple" == "apple")   # Case-sensitive
print("a" < "b")

# ============================================================
#               LOOPING THROUGH STRING
# ============================================================

for ch in "Python":
    print(ch)

# ============================================================
#               REAL-LIFE EXAMPLES
# ============================================================

# ------------------------------------------------------------
# Example 1: Check palindrome
# ------------------------------------------------------------

word = "madam"
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# ------------------------------------------------------------
# Example 2: Count vowels
# ------------------------------------------------------------

text = "python programming"
vowels = "aeiou"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Vowel count:", count)

# ------------------------------------------------------------
# Example 3: Password validation
# ------------------------------------------------------------

password = "Python123"

if password.isalnum() and len(password) >= 6:
    print("Valid password")
else:
    print("Invalid password")

# ============================================================
#               IMPORTANT POINTS
# ============================================================

# 1. Strings are immutable
# 2. Indexing starts from 0
# 3. Negative indexing starts from -1
# 4. f-strings are fastest and cleanest
# 5. Use string methods to manipulate text

# ============================================================
# End of File: 012 Strings.py
# ============================================================
