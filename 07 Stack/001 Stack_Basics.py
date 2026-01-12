# ============================================================
#                     STACK – BASICS (PYTHON)
# ============================================================

# Stack is a LINEAR data structure
# that follows the principle:
# LIFO → Last In, First Out

# Example (real life):
# - Stack of plates
# - Undo / Redo
# - Browser back button
# - Function call stack

# ============================================================
#                     STACK OPERATIONS
# ============================================================

# 1. Push   → Add element
# 2. Pop    → Remove top element
# 3. Peek   → View top element
# 4. isEmpty
# 5. Size

# ============================================================
#                     IMPLEMENTATION 1
#             STACK USING PYTHON LIST (MOST COMMON)
# ============================================================

stack = []

# ---------------- PUSH ----------------
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after push:", stack)

# ---------------- POP -----------------
top = stack.pop()
print("Popped element:", top)
print("Stack after pop:", stack)

# ---------------- PEEK ----------------
if stack:
    print("Top element:", stack[-1])

# ---------------- isEmpty -------------
print("Is stack empty?", len(stack) == 0)

# ============================================================
#                     TIME COMPLEXITY
# ============================================================

# Push  → O(1)
# Pop   → O(1)
# Peek  → O(1)

# ============================================================
#             IMPLEMENTATION 2
#        STACK USING CUSTOM CLASS (INTERVIEW STYLE)
# ============================================================

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        print("Stack (top -> bottom):", self.items[::-1])

# ============================================================
#                     TESTING STACK CLASS
# ============================================================

s = Stack()

s.push(5)
s.push(10)
s.push(15)

s.display()

print("Peek:", s.peek())
print("Pop:", s.pop())

s.display()

print("Is Empty:", s.is_empty())
print("Size:", s.size())

# ============================================================
#                     STACK USING collections.deque
# ============================================================

from collections import deque

stack = deque()

stack.append(100)
stack.append(200)
stack.append(300)

print("Deque Stack:", stack)

stack.pop()
print("After pop:", stack)

# ============================================================
#                     WHERE STACK IS USED
# ============================================================

# 1. Function calls (call stack)
# 2. Expression evaluation
# 3. Undo / Redo
# 4. Parenthesis checking
# 5. Backtracking
# 6. Depth First Search (DFS)

# ============================================================
#                     COMMON STACK PROBLEMS
# ============================================================

# - Reverse a string
# - Valid parentheses
# - Next Greater Element
# - Infix → Postfix
# - Evaluate postfix expression

# ============================================================
#                     THINKING RULE (IMPORTANT)
# ============================================================

# If a problem involves:
# - Undo / Redo
# - Nearest element
# - Previous state
# - Reversal
# 👉 THINK STACK

# ============================================================
# End of File: 050 Stack_Basics.py
# ============================================================
