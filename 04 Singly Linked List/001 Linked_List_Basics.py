# ============================================================
#                 LINKED LIST – BASICS (PYTHON)
# ============================================================

# A Linked List is a LINEAR data structure
# where elements (nodes) are NOT stored in contiguous memory.

# Each node contains:
# 1. Data
# 2. Reference (pointer) to the next node

# ============================================================
#                 WHY LINKED LIST?
# ============================================================

# Arrays problems:
# ❌ Fixed size
# ❌ Expensive insertion/deletion

# Linked List advantages:
# ✅ Dynamic size
# ✅ Easy insertion/deletion (no shifting)

# ============================================================
#                 LINKED LIST TYPES
# ============================================================

# 1. Singly Linked List
# 2. Doubly Linked List
# 3. Circular Linked List

# In this file → Singly Linked List (MOST IMPORTANT)

# ============================================================
#                 NODE STRUCTURE
# ============================================================

class Node:
    def __init__(self, data):
        self.data = data      # Store value
        self.next = None      # Reference to next node

# ============================================================
#                 LINKED LIST STRUCTURE
# ============================================================

class LinkedList:
    def __init__(self):
        self.head = None      # Head points to first node

    # ========================================================
    #                 INSERT AT END
    # ========================================================

    def append(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            return

        # Traverse to last node
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # ========================================================
    #                 INSERT AT BEGINNING
    # ========================================================

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # ========================================================
    #                 DELETE A NODE (BY VALUE)
    # ========================================================

    def delete(self, key):
        temp = self.head

        # If head node itself holds key
        if temp and temp.data == key:
            self.head = temp.next
            return

        # Search for key
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next

    # ========================================================
    #                 TRAVERSE / DISPLAY
    # ========================================================

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # ========================================================
    #                 SEARCH ELEMENT
    # ========================================================

    def search(self, key):
        temp = self.head
        position = 0

        while temp:
            if temp.data == key:
                return position
            temp = temp.next
            position += 1

        return -1

# ============================================================
#                 USING THE LINKED LIST
# ============================================================

ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)

ll.insert_at_beginning(5)

ll.display()

print("Search 20:", ll.search(20))

ll.delete(20)
ll.display()

# ============================================================
#                 TIME COMPLEXITY (IMPORTANT)
# ============================================================

# Access      → O(n)
# Search      → O(n)
# Insert head → O(1)
# Insert tail → O(n)
# Delete      → O(n)

# ============================================================
#                 ARRAY vs LINKED LIST
# ============================================================

# +-------------------+-------------+------------------+
# | Feature           | Array       | Linked List     |
# +-------------------+-------------+------------------+
# | Memory            | Contiguous  | Non-contiguous  |
# | Size              | Fixed       | Dynamic         |
# | Access            | O(1)        | O(n)            |
# | Insert/Delete     | Expensive   | Efficient       |
# +-------------------+-------------+------------------+

# ============================================================
#                 COMMON MISTAKES
# ============================================================

# 1. Forgetting to update head
# 2. Losing reference to nodes
# 3. Incorrect loop conditions
# 4. Not handling empty list

# ============================================================
#                 THINKING TIPS (VERY IMPORTANT)
# ============================================================

# Always draw Linked List on paper:
# head -> [data | next] -> [data | next] -> None

# ============================================================
# End of File: 001 Linked_List_Basics.py
# ============================================================
