# ============================================================
#        LINKED LIST – INTERVIEW PROBLEMS (PYTHON)
# ============================================================

# This file contains:
# - Most asked Linked List interview problems
# - Pattern-based solutions
# - Clean, readable, and optimized code
# - Focus on THINKING, not memorization

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
        if not self.head:
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
    # INTERVIEW PROBLEM 1:
    # DETECT CYCLE IN LINKED LIST
    # ========================================================

    def detect_cycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    # ========================================================
    # INTERVIEW PROBLEM 2:
    # FIND START OF CYCLE
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
            return None

        # Step 2: Move slow to head
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow.data

    # ========================================================
    # INTERVIEW PROBLEM 3:
    # REVERSE LINKED LIST (ITERATIVE)
    # ========================================================

    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev

    # ========================================================
    # INTERVIEW PROBLEM 4:
    # CHECK IF LINKED LIST IS PALINDROME
    # ========================================================

    def is_palindrome(self):
        slow = self.head
        fast = self.head

        # Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Compare halves
        left = self.head
        right = prev

        while right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next

        return True

    # ========================================================
    # INTERVIEW PROBLEM 5:
    # REMOVE NTH NODE FROM END
    # ========================================================

    def remove_nth_from_end(self, n):
        dummy = Node(0)
        dummy.next = self.head
        slow = dummy
        fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        self.head = dummy.next

    # ========================================================
    # INTERVIEW PROBLEM 6:
    # INTERSECTION OF TWO LINKED LISTS
    # ========================================================

    @staticmethod
    def get_intersection(head1, head2):
        p1, p2 = head1, head2

        while p1 != p2:
            p1 = p1.next if p1 else head2
            p2 = p2.next if p2 else head1

        return p1.data if p1 else None

    # ========================================================
    # INTERVIEW PROBLEM 7:
    # MERGE TWO SORTED LINKED LISTS
    # ========================================================

    @staticmethod
    def merge_sorted(l1, l2):
        dummy = Node(0)
        curr = dummy

        while l1 and l2:
            if l1.data < l2.data:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 if l1 else l2
        return dummy.next

    # ========================================================
    # INTERVIEW PROBLEM 8:
    # SWAP NODES IN PAIRS
    # ========================================================

    def swap_pairs(self):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first

        self.head = dummy.next

    # ========================================================
    # INTER
