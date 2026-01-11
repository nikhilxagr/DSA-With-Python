# ============================================================
#          LINKED LIST PROBLEMS – LEVEL 1 (PYTHON)
# ============================================================

# Goal of this file:
# - Strengthen Linked List basics
# - Build pointer/reference thinking
# - Prepare for interviews & DSA problems

# ============================================================
#          NODE DEFINITION
# ============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# ============================================================
#          LINKED LIST CLASS
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
    # PROBLEM 1: FIND LENGTH OF LINKED LIST
    # ========================================================

    def length(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count

    # ========================================================
    # PROBLEM 2: SEARCH AN ELEMENT
    # ========================================================

    def search(self, key):
        temp = self.head
        pos = 0

        while temp:
            if temp.data == key:
                return pos
            temp = temp.next
            pos += 1

        return -1

    # ========================================================
    # PROBLEM 3: DELETE FIRST NODE
    # ========================================================

    def delete_first(self):
        if self.head is None:
            return

        self.head = self.head.next

    # ========================================================
    # PROBLEM 4: DELETE LAST NODE
    # ========================================================

    def delete_last(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None

    # ========================================================
    # PROBLEM 5: DELETE NODE BY VALUE
    # ========================================================

    def delete_by_value(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next

    # ========================================================
    # PROBLEM 6: REVERSE LINKED LIST (ITERATIVE)
    # ========================================================

    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

    # ========================================================
    # PROBLEM 7: FIND MIDDLE OF LINKED LIST
    # ========================================================

    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data if slow else None

    # ========================================================
    # PROBLEM 8: COUNT OCCURRENCE OF A VALUE
    # ========================================================

    def count_occurrence(self, key):
        count = 0
        temp = self.head

        while temp:
            if temp.data == key:
                count += 1
            temp = temp.next

        return count

    # ========================================================
    # PROBLEM 9: CHECK IF LINKED LIST IS EMPTY
    # ========================================================

    def is_empty(self):
        return self.head is None

    # ========================================================
    # PROBLEM 10: CONVERT LINKED LIST TO PYTHON LIST
    # ========================================================

    def to_list(self):
        result = []
        temp = self.head

        while temp:
            result.append(temp.data)
            temp = temp.next

        return result


# ============================================================
#          TESTING ALL PROBLEMS
# ============================================================

ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(20)
ll.append(40)

ll.display()

print("Length:", ll.length())
print("Search 30:", ll.search(30))
print("Occurrences of 20:", ll.count_occurrence(20))
print("Middle:", ll.find_middle())

ll.delete_first()
ll.display()

ll.delete_last()
ll.display()

ll.delete_by_value(20)
ll.display()

ll.reverse()
ll.display()

print("Is Empty:", ll.is_empty())
print("As Python List:", ll.to_list())

# ============================================================
#          IMPORTANT TAKEAWAYS
# ============================================================

# 1. Traversal is the base of all LL problems
# 2. Always handle empty list & single node
# 3. Use slow-fast pointer for middle problems
# 4. Reverse LL is an INTERVIEW MUST
# 5. Practice drawing pointers on paper

# ============================================================
# End of File: 003 Linked_List_Problems_Level1.py
# ============================================================
