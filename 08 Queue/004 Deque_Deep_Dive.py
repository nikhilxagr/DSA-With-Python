# ============================================================
#                 DEQUE – DEEP DIVE (PYTHON)
# ============================================================

# Deque stands for:
# DOUBLE ENDED QUEUE

# It allows insertion and deletion from:
# - FRONT
# - REAR

# Deque is implemented in Python using:
# collections.deque  (highly optimized)

# ============================================================
#                 WHY DEQUE IS IMPORTANT?
# ============================================================

# 1. Faster than list for queue operations
# 2. Can act as Stack and Queue
# 3. Used in sliding window problems
# 4. Used in BFS, caching, scheduling
# 5. Interview favorite

# ============================================================
#                 IMPORT DEQUE
# ============================================================

from collections import deque

# ============================================================
#                 BASIC DEQUE CREATION
# ============================================================

dq = deque()

dq.append(10)        # Add at right
dq.append(20)
dq.appendleft(5)     # Add at left

print("Deque:", dq)

# ============================================================
#                 DEQUE REMOVAL
# ============================================================

dq.pop()             # Remove from right
dq.popleft()         # Remove from left

print("After removals:", dq)

# ============================================================
#                 DEQUE OPERATIONS SUMMARY
# ============================================================

# append(x)       → Insert at right
# appendleft(x)   → Insert at left
# pop()           → Remove from right
# popleft()       → Remove from left

# All operations → O(1)

# ============================================================
#                 ACCESS ELEMENTS
# ============================================================

dq.append(100)
dq.append(200)
dq.append(300)

print("Front element:", dq[0])
print("Rear element:", dq[-1])

# ============================================================
#                 DEQUE AS STACK
# ============================================================

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)

print("Stack:", stack)

stack.pop()
print("After pop:", stack)

# ============================================================
#                 DEQUE AS QUEUE
# ============================================================

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

print("Queue:", queue)

queue.popleft()
print("After dequeue:", queue)

# ============================================================
#                 MAX SIZE DEQUE
# ============================================================

dq = deque(maxlen=3)

dq.append(10)
dq.append(20)
dq.append(30)
dq.append(40)  # Oldest element removed automatically

print("Fixed size deque:", dq)

# ============================================================
#                 ROTATE DEQUE
# ============================================================

dq = deque([1, 2, 3, 4, 5])

dq.rotate(1)     # Rotate right
print("Rotate right:", dq)

dq.rotate(-2)    # Rotate left
print("Rotate left:", dq)

# ============================================================
#                 REVERSE DEQUE
# ============================================================

dq.reverse()
print("Reversed deque:", dq)

# ============================================================
#                 SLIDING WINDOW PROBLEM (IMPORTANT)
# ============================================================

# Problem:
# Given array and window size k
# Find maximum in each window

def sliding_window_max(nums, k):
    dq = deque()
    result = []

    for i in range(len(nums)):
        # Remove out-of-window elements
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller elements
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

print(sliding_window_max([1,3,-1,-3,5,3,6,7], 3))

# Time → O(n)
# Space → O(k)

# ============================================================
#                 MONOTONIC DEQUE (ADVANCED)
# ============================================================

# Deque that maintains increasing or decreasing order
# Used in:
# - Sliding window
# - Stock span
# - Next greater/smaller element

# ============================================================
#                 PALINDROME CHECK USING DEQUE
# ============================================================

def is_palindrome(s):
    dq = deque(s)

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

print(is_palindrome("radar"))
print(is_palindrome("python"))

# ============================================================
#                 DEQUE VS LIST VS STACK
# ============================================================

# +------------+-----------+-----------+
# | Feature    | List      | Deque     |
# +------------+-----------+-----------+
# | Append     | O(1)      | O(1)      |
# | Pop end    | O(1)      | O(1)      |
# | Pop front  | O(n) ❌   | O(1) ✅   |
# | Rotate     | ❌        | ✅        |
# +------------+-----------+-----------+

# ============================================================
#                 COMMON MISTAKES
# ============================================================

# 1. Using list instead of deque for queue
# 2. Forgetting popleft() vs pop()
# 3. Not removing out-of-window elements
# 4. Confusing indices vs values in sliding window

# ============================================================
#                 INTERVIEW THINKING RULE
# ============================================================

# If a problem involves:
# - Sliding window
# - Max/min in range
# - Front & rear operations
# 👉 THINK DEQUE FIRST

# ============================================================
# End of File: 056 Deque_Deep_Dive.py
# ============================================================
