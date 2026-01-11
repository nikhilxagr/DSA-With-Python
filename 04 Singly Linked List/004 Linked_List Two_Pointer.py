# ============================================================
#        LINKED LIST – TWO POINTER PATTERN (PYTHON)
# ============================================================

# Two Pointer (Slow & Fast) is the MOST IMPORTANT
# pattern for Linked List problems.

# Also called:
# - Tortoise & Hare Algorithm
# - Floyd’s Cycle Algorithm

# ============================================================
#        WHY TWO POINTER PATTERN?
# ============================================================

# Used to:
# 1. Find middle of linked list
# 2. Detect cycle
# 3. Find starting point of cycle
# 4. Check palindrome
# 5. Remove nth node from end

# ============================================================
#        NODE DEFINITION
# ============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# ============================================================
#        LINKED LIST CLASS
# ============================================================

class LinkedList:
    def __init__(self):
        self.head = None

    # --------------------------------------------------------
    # Insert at end
    # --------------------------------------------------------
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # --------------------------------------------------------
    # Display list
    # --------------------------------------------------------
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # ========================================================
    # PROBLEM 1: FIND MIDDLE OF LINKED LIST
    # ========================================================

    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data if slow else None

    # ========================================================
    # PROBLEM 2: DETECT CYCLE (FLOYD'S ALGORITHM)
    # ========================================================

    def has_cycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    # ========================================================
    # PROBLEM 3: FIND STARTING POINT OF CYCLE
    # ========================================================

    def find_cycle_start(self):
        slow = self.head
        fast = self.head

        # Step 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None  # No cycle

        # Step 2: Find start of cycle
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow.data

    # ========================================================
    # PROBLEM 4: REMOVE NTH NODE FROM END
    # ========================================================

    def remove_nth_from_end(self, n):
        dummy = Node(0)
        dummy.next = self.head
        slow = dummy
        fast = dummy

        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both pointers
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        self.head = dummy.next

    # ========================================================
    # PROBLEM 5: CHECK IF LINKED LIST IS PALINDROME
    # ========================================================

    def is_palindrome(self):
        # Step 1: Find middle
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: Compare both halves
        left = self.head
        right = prev

        while right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next

        return True


# ============================================================
#        TESTING TWO POINTER PROBLEMS
# ============================================================

ll = LinkedList()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(2)
ll.append(1)

ll.display()

print("Middle:", ll.find_middle())
print("Is Palindrome:", ll.is_palindrome())

# Create cycle for testing
ll.head.next.next.next.next = ll.head.next

print("Has Cycle:", ll.has_cycle())
print("Cycle Starts At:", ll.find_cycle_start())

# ============================================================
#        TIME & SPACE COMPLEXITY
# ============================================================

# All Two Pointer problems:
# Time  → O(n)
# Space → O(1)

# ============================================================
#        THINKING RULE (MUST REMEMBER)
# ============================================================

# If a problem involves:
# - Middle
# - Cycle
# - From end
# - Palindrome
# 👉 THINK TWO POINTER FIRST

# ============================================================
# End of File: 004 Linked_List_Two_Pointer.py
# ============================================================
