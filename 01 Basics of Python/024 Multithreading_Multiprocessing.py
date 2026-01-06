# ============================================================
#        MULTITHREADING & MULTIPROCESSING IN PYTHON
# ============================================================

# Multithreading and Multiprocessing are used to
# execute multiple tasks at the same time (concurrency).

# They help to:
# - Improve performance
# - Reduce execution time
# - Efficiently use system resources

# ============================================================
#        THREAD vs PROCESS (SUMMARY TABLE)
# ============================================================

# +-------------------+------------------------+-------------------------+
# | Feature           | Multithreading         | Multiprocessing         |
# +-------------------+------------------------+-------------------------+
# | Unit              | Thread                 | Process                 |
# | Memory            | Shared                 | Separate                |
# | Speed             | Faster creation        | Slower creation         |
# | CPU Bound Tasks   | ❌ Not efficient       | ✅ Efficient            |
# | I/O Bound Tasks   | ✅ Efficient           | ❌ Overkill             |
# | GIL Impact        | Yes                    | No                      |
# +-------------------+------------------------+-------------------------+

# ============================================================
#        WHAT IS GIL (GLOBAL INTERPRETER LOCK)?
# ============================================================

# GIL allows only ONE thread to execute Python bytecode at a time
# This affects CPU-bound multithreaded programs

# NOTE:
# - Multithreading is best for I/O-bound tasks
# - Multiprocessing is best for CPU-bound tasks

# ============================================================
#        1. MULTITHREADING
# ============================================================

# A thread is a lightweight unit of execution
# Multiple threads share the same memory

import threading
import time

# ============================================================
#        BASIC THREAD EXAMPLE
# ============================================================

def task():
    print("Task started")
    time.sleep(2)
    print("Task completed")

t1 = threading.Thread(target=task)
t1.start()
t1.join()   # Wait for thread to finish

print("Main thread finished")

# ============================================================
#        MULTIPLE THREADS
# ============================================================

def print_numbers():
    for i in range(1, 6):
        print("Number:", i)
        time.sleep(1)

def print_letters():
    for ch in "ABCDE":
        print("Letter:", ch)
        time.sleep(1)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()

print("Both threads completed")

# ============================================================
#        THREAD WITH ARGUMENTS
# ============================================================

def greet(name):
    print("Hello", name)

t = threading.Thread(target=greet, args=("Rahul",))
t.start()
t.join()

# ============================================================
#        THREAD CLASS (CUSTOM THREAD)
# ============================================================

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            print("Running thread")
            time.sleep(1)

t = MyThread()
t.start()
t.join()

# ============================================================
#        THREAD SYNCHRONIZATION (LOCK)
# ============================================================

# Lock prevents race conditions

lock = threading.Lock()
counter = 0

def increment():
    global counter
    with lock:
        for _ in range(100000):
            counter += 1

threads = []

for i in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Counter value:", counter)

# ============================================================
#        REAL-LIFE MULTITHREADING EXAMPLE
# ============================================================

# Downloading multiple files (simulation)

def download(file):
    print(f"Downloading {file}")
    time.sleep(2)
    print(f"{file} downloaded")

files = ["file1", "file2", "file3"]

threads = []

for f in files:
    t = threading.Thread(target=download, args=(f,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All downloads completed")

# ============================================================
#        2. MULTIPROCESSING
# ============================================================

# Multiprocessing creates separate processes
# Each process has its own memory space
# Best for CPU-bound tasks

import multiprocessing

# ============================================================
#        BASIC PROCESS EXAMPLE
# ============================================================

def square(num):
    print("Square:", num * num)

p = multiprocessing.Process(target=square, args=(5,))
p.start()
p.join()

# ============================================================
#        MULTIPLE PROCESSES
# ============================================================

def cube(num):
    print("Cube:", num ** 3)

processes = []

for i in range(1, 5):
    p = multiprocessing.Process(target=cube, args=(i,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

print("All processes completed")

# ============================================================
#        USING multiprocessing.Pool
# ============================================================

def square(num):
    return num * num

with multiprocessing.Pool(processes=4) as pool:
    result = pool.map(square, [1, 2, 3, 4, 5])

print("Squares:", result)

# ============================================================
#        SHARING DATA BETWEEN PROCESSES
# ============================================================

# Using Value & Array

def increment_shared(val):
    for _ in range(100):
        val.value += 1

shared_value = multiprocessing.Value('i', 0)

p1 = multiprocessing.Process(target=increment_shared, args=(shared_value,))
p2 = multiprocessing.Process(target=increment_shared, args=(shared_value,))

p1.start()
p2.start()

p1.join()
p2.join()

print("Shared value:", shared_value.value)

# ============================================================
#        REAL-LIFE MULTIPROCESSING EXAMPLE
# ============================================================

# CPU-intensive task (factorial)

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

numbers = [5, 6, 7, 8]

with multiprocessing.Pool() as pool:
    results = pool.map(factorial, numbers)

print("Factorials:", results)

# ============================================================
#        COMMON MISTAKES
# ============================================================

# 1. Using threads for CPU-bound tasks
# 2. Forgetting if __name__ == "__main__" (Windows issue)
# 3. Not using join() → zombie threads/processes
# 4. Sharing mutable data without synchronization

# ============================================================
#        IMPORTANT POINTS
# ============================================================

# 1. Use multithreading for I/O-bound tasks
# 2. Use multiprocessing for CPU-bound tasks
# 3. GIL affects multithreading
# 4. Processes consume more memory than threads
# 5. Always test performance before optimizing

# ============================================================
# End of File: 024 Multithreading_Multiprocessing.py
# ============================================================
