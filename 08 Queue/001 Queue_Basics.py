# ============================================================
#                     QUEUE – BASICS (PYTHON)
# ============================================================

# Queue is a LINEAR data structure
# that follows the principle:
# FIFO → First In, First Out

# Real-life examples:
# - Line at ticket counter
# - CPU task scheduling
# - Printer queue
# - Call center systems

# ============================================================
#                     QUEUE OPERATIONS
# ============================================================

# 1. Enqueue  → Insert element at rear
# 2. Dequeue  → Remove element from front
# 3. Front    → Get front element
# 4. Rear     → Get last element
# 5. isEmpty
# 6. Size

# ============================================================
#              IMPLEMENTATION 1
#        QUEUE USING PYTHON LIST (NOT OPTIMAL)
# ============================================================

queue = []

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)

# Dequeue (slow ❌)
removed = queue.pop(0)
print("Removed:", removed)
print("Queue after dequeue:", queue)

# Time Complexity:
# Enqueue → O(1)
# Dequeue → O(n) ❌ (shifting elements)

# ============================================================
#              IMPLEMENTATION 2 (BEST)
#        QUEUE USING collections.deque
# ============================================================

from collections import deque

queue = deque()

# Enqueue
queue.append(100)
queue.append(200)
queue.append(300)

print("Deque Queue:", queue)

# Dequeue
print("Dequeued:", queue.popleft())
print("Queue after dequeue:", queue)

# Time Complexity:
# Enqueue → O(1)
# Dequeue → O(1)

# ============================================================
#              IMPLEMENTATION 3
#        QUEUE USING CUSTOM CLASS (INTERVIEW STYLE)
# ============================================================

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        return self.items.popleft()

    def front(self):
        if self.is_empty():
            return None
        return self.items[0]

    def rear(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        print("Queue (front -> rear):", list(self.items))

# ============================================================
#                     TESTING QUEUE CLASS
# ============================================================

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

q.display()

print("Front:", q.front())
print("Rear:", q.rear())

print("Dequeued:", q.dequeue())
q.display()

print("Is Empty:", q.is_empty())
print("Size:", q.size())

# ============================================================
#                     TIME COMPLEXITY
# ============================================================

# Enqueue → O(1)
# Dequeue → O(1)
# Front   → O(1)
# Rear    → O(1)

# ============================================================
#                     TYPES OF QUEUES
# ============================================================

# 1. Simple Queue
# 2. Circular Queue
# 3. Priority Queue
# 4. Deque (Double Ended Queue)

# ============================================================
#                     WHERE QUEUE IS USED
# ============================================================

# 1. CPU Scheduling
# 2. Breadth First Search (BFS)
# 3. Task queues
# 4. Producer–Consumer problem
# 5. Networking (packet handling)

# ============================================================
#                     STACK vs QUEUE
# ============================================================

# +------------+-----------+-----------+
# | Feature    | Stack     | Queue     |
# +------------+-----------+-----------+
# | Principle  | LIFO      | FIFO      |
# | Insert     | Top       | Rear      |
# | Remove     | Top       | Front     |
# | Use case   | Undo      | Scheduling|
# +------------+-----------+-----------+

# ============================================================
#                     THINKING RULE (IMPORTANT)
# ============================================================

# If a problem involves:
# - Order of processing
# - First come, first serve
# - Level-by-level traversal
# 👉 THINK QUEUE

# ============================================================
# End of File: 001 Queue_Basics.py
# ============================================================
