# ============================================================
#        LINKED LIST PROBLEMS – LEVEL 2 (PYTHON)
# ============================================================

# Level 2 goals:
# - Master pointer manipulation
# - Combine multiple concepts
# - Think in patterns (not steps)
# - Prepare for interview-style problems

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
    # PROBLEM 1: REVERSE LINKED LIST (RECURSIVE)
    # ========================================================

    def reverse_recursive(self):
        def helper(curr, prev):
            if not curr:
                return prev
            next_node = curr.next
            curr.next = prev
            return helper(next_node, curr)

        self.head = helper(self.head, None)

    # ========================================================
    # PROBLEM 2: REMOVE DUPLICATES (UNSORTED LIST)
    # ========================================================

    def remove_duplicates_unsorted(self):
        seen = set()
        curr = self.head
        prev = None

        while curr:
            if curr.data in seen:
                prev.next = curr.next
            else:
                seen.add(curr.data)
                prev = curr
            curr = curr.next

    # Time → O(n)
    # Space → O(n)

    # ========================================================
    # PROBLEM 3: NTH NODE FROM END (WITHOUT LENGTH)
    # ========================================================

    def nth_from_end(self, n):
        slow = self.head
        fast = self.head

        for _ in range(n):
            if not fast:
                return None
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        return slow.data if slow else None

    # ========================================================
    # PROBLEM 4: INTERSECTION OF TWO LINKED LISTS
    # ========================================================

    @staticmethod
    def get_intersection(head1, head2):
        p1, p2 = head1, head2

        while p1 != p2:
            p1 = p1.next if p1 else head2
            p2 = p2.next if p2 else head1

        return p1.data if p1 else None

    # ========================================================
    # PROBLEM 5: ADD TWO NUMBERS (LL REPRESENTATION)
    # Example: 2 -> 4 -> 3
    #        + 5 -> 6 -> 4
    #        = 7 -> 0 -> 8
    # ========================================================

    @staticmethod
    def add_two_lists(l1, l2):
        dummy = Node(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.data
                l1 = l1.next
            if l2:
                total += l2.data
                l2 = l2.next

            carry = total // 10
            curr.next = Node(total % 10)
            curr = curr.next

        return dummy.next

    # ========================================================
    # PROBLEM 6: ODD EVEN LINKED LIST
    # ========================================================

    def odd_even_list(self):
        if not self.head:
            return

        odd = self.head
        even = self.head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head

    # ========================================================
    # PROBLEM 7: SWAP NODES IN PAIRS
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

# ============================================================
#        TESTING LEVEL 2 PROBLEMS
# ============================================================

ll = LinkedList()
for val in [1, 2, 3, 4, 3, 2, 1]:
    ll.append(val)

print("Original:")
ll.display()

print("\nReverse Recursive:")
ll.reverse_recursive()
ll.display()

print("\nRemove Duplicates (Unsorted):")
ll.remove_duplicates_unsorted()
ll.display()

print("\n3rd Node from End:", ll.nth_from_end(3))

print("\nOdd-Even Arrangement:")
ll.odd_even_list()
ll.display()

print("\nSwap Nodes in Pairs:")
ll.swap_pairs()
ll.display()

# ============================================================
#        IMPORTANT INTERVIEW PATTERNS USED
# ============================================================

# 1. Two Pointer (slow-fast)
# 2. Dummy Node technique
# 3. Hashing for duplicates
# 4. Pointer rewiring
# 5. Recursion for reversal

# ============================================================
#        INTERVIEW THINKING CHECKLIST
# ============================================================

# Ask yourself:
# 1. Do I need extra space?
# 2. Can I solve in one pass?
# 3. Do I need a dummy node?
# 4. Is recursion safe here?
# 5. What edge cases exist?

# ============================================================
# End of File: 046 Linked_List_Level2_Problems.py
# ============================================================
