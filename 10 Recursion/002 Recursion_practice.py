# Fatorial of a number using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))  # Output: 120


# Fibonacci sequence using recursion

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(7))  # Output: 13

# Sum of digits of a number using recursion

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)
print(sum_of_digits(1234))  # Output: 10

# Reverse a string using recursion

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])
print(reverse_string("hello"))  # Output: "olleh"