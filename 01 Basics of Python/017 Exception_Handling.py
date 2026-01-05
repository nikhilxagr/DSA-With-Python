# ============================================================
#               EXCEPTION HANDLING IN PYTHON
# ============================================================

# An exception is a runtime error that disrupts
# the normal flow of a program.

# Exception handling allows us to:
# - Prevent program crash
# - Handle errors gracefully
# - Show meaningful error messages

# ============================================================
#               EXCEPTION HANDLING SUMMARY TABLE
# ============================================================

# +------------------+----------------------------------------+
# | Keyword          | Description                            |
# +------------------+----------------------------------------+
# | try              | Code that may cause error              |
# | except           | Handles the error                      |
# | else             | Runs if no exception occurs            |
# | finally          | Always runs (cleanup code)             |
# | raise            | Manually raise an exception            |
# +------------------+----------------------------------------+

# ============================================================
#               WHY EXCEPTION HANDLING IS NEEDED
# ============================================================

# Without exception handling → program crashes
# With exception handling → program continues safely

# ============================================================
#               BASIC EXAMPLE (WITHOUT HANDLING)
# ============================================================

# x = 10 / 0   # ❌ ZeroDivisionError

# ============================================================
#               BASIC TRY - EXCEPT
# ============================================================

try:
    x = 10 / 0
except:
    print("Error occurred")

# ============================================================
#               HANDLING SPECIFIC EXCEPTIONS
# ============================================================

try:
    a = int("Python")
except ValueError:
    print("ValueError: Invalid conversion")
except ZeroDivisionError:
    print("ZeroDivisionError occurred")

# ============================================================
#               MULTIPLE EXCEPTIONS TOGETHER
# ============================================================

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero")

# ============================================================
#               TRY - EXCEPT - ELSE
# ============================================================

try:
    num = int(input("Enter number: "))
    result = 100 / num
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result:", result)

# ============================================================
#               TRY - EXCEPT - FINALLY
# ============================================================

try:
    file = open("demo.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution completed")

# ============================================================
#               USING ELSE AND FINALLY TOGETHER
# ============================================================

try:
    x = int(input("Enter value: "))
except ValueError:
    print("Invalid input")
else:
    print("You entered:", x)
finally:
    print("Program ended")

# ============================================================
#               RAISING EXCEPTIONS (raise)
# ============================================================

age = int(input("Enter age: "))

if age < 18:
    raise ValueError("Age must be 18 or above")

print("Access granted")

# ============================================================
#               CUSTOM EXCEPTION
# ============================================================

class InsufficientBalanceError(Exception):
    pass

balance = 500

try:
    withdraw = int(input("Enter withdrawal amount: "))
    if withdraw > balance:
        raise InsufficientBalanceError("Not enough balance")
    balance -= withdraw
    print("Remaining balance:", balance)
except InsufficientBalanceError as e:
    print("Error:", e)

# ============================================================
#               COMMON BUILT-IN EXCEPTIONS
# ============================================================

# ZeroDivisionError
# ValueError
# TypeError
# IndexError
# KeyError
# FileNotFoundError
# NameError

# ============================================================
#               REAL-LIFE EXAMPLES
# ============================================================

# ------------------------------------------------------------
# Example 1: Safe calculator
# ------------------------------------------------------------

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter valid numbers")

# ------------------------------------------------------------
# Example 2: Dictionary key access
# ------------------------------------------------------------

data = {"name": "Rahul", "age": 21}

try:
    print(data["salary"])
except KeyError:
    print("Key does not exist")

# ------------------------------------------------------------
# Example 3: File handling with exception
# ------------------------------------------------------------

try:
    with open("records.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("records.txt file not found")

# ============================================================
#               COMMON MISTAKES
# ============================================================

# 1. Using except without specifying exception (bad practice)
# 2. Catching all exceptions unnecessarily
# 3. Ignoring exception messages
# 4. Not using finally for cleanup

# ============================================================
#               IMPORTANT POINTS
# ============================================================

# 1. Exceptions occur at runtime
# 2. Always handle specific exceptions
# 3. finally block always executes
# 4. raise is used for custom errors
# 5. Exception handling improves program reliability

# ============================================================
# End of File: 017 Exception_Handling.py
# ============================================================
