# ============================================================
#              CIRCULAR QUEUE – BASICS (PYTHON)
# ============================================================

# Circular Queue is a linear data structure
# that follows FIFO (First In First Out)
# but connects the last position back to the first.

# Instead of:
# front -> [ ][ ][ ][ ] -> rear -> None
#
# It becomes:
# front -> [ ][ ][ ][ ] <- rear
#            ^__________|

# ============================================================
#              WHY CIRCULAR QUEUE?
# ============================================================

# Problem with normal queue (array-based):
# ❌ Wasted space after dequeue
# ❌ Rear reaches end even if front has space

# Circular Queue solves this by:
# ✅ Reusing empty spaces
# ✅ Wrapping rear to start

# ============================================================
#              KEY TERMS
# ============================================================

# front → index of first element
# rear  → index of last element
# size  → max size of queue

# Queue is:
# Empty when → front == -1
# Full when  → (rear + 1) % size == front

# ============================================================
#              CIRCULAR QUEUE IMPLEMENTATION
# ============================================================

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # ========================================================
    #              CHECK IF QUEUE IS EMPTY
    # ========================================================
    def is_empty(self):
        return self.front == -1

    # ========================================================
    #              CHECK IF QUEUE IS FULL
    # ========================================================
    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    # ========================================================
    #              ENQUEUE OPERATION
    # ========================================================
    def enqueue(self, value):
        if self.is_full():
            print("Queue Overflow")
            return

        # First insertion
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = value
        print(f"Enqueued: {value}")

    # ========================================================
    #              DEQUEUE OPERATION
    # ========================================================
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None

        value = self.queue[self.front]

        # Only one element
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(f"Dequeued: {value}")
        return value

    # ========================================================
    #              DISPLAY QUEUE
    # ========================================================
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        print("Circular Queue:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

# ============================================================
#              TESTING CIRCULAR QUEUE
# ============================================================

cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)

cq.display()

cq.dequeue()
cq.dequeue()

cq.display()

cq.enqueue(60)
cq.enqueue(70)

cq.display()

# ============================================================
#              TIME COMPLEXITY
# ============================================================

# Enqueue → O(1)
# Dequeue → O(1)
# Display → O(n)

# ============================================================
#              QUEUE TYPES COMPARISON
# ============================================================

# +------------------+---------------------+
# | Queue Type       | 특징 / Feature      |
# +------------------+---------------------+
# | Simple Queue     | Wastes space        |
# | Circular Queue   | Space efficient     |
# | Deque            | Insert both ends    |
# | Priority Queue   | Priority based      |
# +------------------+---------------------+

# ============================================================
#              REAL-LIFE USE CASES
# ============================================================

# 1. CPU Scheduling (Round Robin)
# 2. Memory management
# 3. Traffic light systems
# 4. Streaming buffers
# 5. Multiplayer games

# ============================================================
#              COMMON MISTAKES (IMPORTANT)
# ============================================================

# 1. Wrong full condition
# 2. Forgetting modulo operation
# 3. Not resetting front & rear
# 4. Infinite loop in display()

# ============================================================
#              THINKING RULE
# ============================================================

# If a problem involves:
# - Fixed size buffer
# - Reusing space
# - Wrap-around logic
# 👉 THINK CIRCULAR QUEUE

# ============================================================
# End of File: 001 Circular_Queue_Basics.py
# ============================================================
