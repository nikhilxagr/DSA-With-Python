# ============================================================
#              CIRCULAR LINKED LIST – BASICS
# ============================================================

# A Circular Linked List (CLL) is a linked list where:
# - The LAST node points back to the FIRST node
# - There is NO None at the end

# head -> [data|next] -> [data|next] -> ... -> head

# ============================================================
#              WHY CIRCULAR LINKED LIST?
# ============================================================

# Advantages:
# ✅ No NULL pointers
# ✅ Efficient traversal from any node
# ✅ Useful in round-robin scheduling
# ✅ Ideal for cyclic data (music playlist, CPU scheduling)

# Disadvantages:
# ❌ Risk of infinite loop if not careful
# ❌ Slightly harder to debug

# ============================================================
#              NODE STRUCTURE
# ============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# ============================================================
#              CIRCULAR LINKED LIST CLASS
# ============================================================

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # ========================================================
    #              INSERT AT END
    # ========================================================

    def append(self, data):
        new_node = Node(data)

        # Case 1: Empty list
        if self.head is None:
            self.head = new_node
            new_node.next = new_node   # Point to itself
            return

        # Case 2: Non-empty list
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    # ========================================================
    #              INSERT AT BEGINNING
    # ========================================================

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    # ========================================================
    #              DELETE A NODE (BY VALUE)
    # ========================================================

    def delete(self, key):
        if self.head is None:
            return

        curr = self.head
        prev = None

        # Case 1: Head node deletion
        if curr.data == key:
            # Only one node
            if curr.next == self.head:
                self.head = None
                return

            # Find last node
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            temp.next = curr.next
            self.head = curr.next
            return

        # Case 2: Delete non-head node
        prev = curr
        curr = curr.next

        while curr != self.head:
            if curr.data == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

        print("Value not found")

    # ========================================================
    #              DISPLAY LIST
    # ========================================================

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

    # ========================================================
    #              SEARCH ELEMENT
    # ========================================================

    def search(self, key):
        if self.head is None:
            return -1

        temp = self.head
        pos = 0

        while True:
            if temp.data == key:
                return pos
            temp = temp.next
            pos += 1
            if temp == self.head:
                break

        return -1

# ============================================================
#              TESTING CIRCULAR LINKED LIST
# ============================================================

cll = CircularLinkedList()

cll.append(10)
cll.append(20)
cll.append(30)

cll.insert_at_beginning(5)

cll.display()

print("Search 20:", cll.search(20))

cll.delete(20)
cll.display()

cll.delete(5)
cll.display()

# ============================================================
#              TIME COMPLEXITY
# ============================================================

# Access/Search → O(n)
# Insert head   → O(n)
# Insert tail   → O(n)
# Delete        → O(n)

# ============================================================
#              SINGLY vs CIRCULAR LINKED LIST
# ============================================================

# +--------------------+-------------------+----------------------+
# | Feature            | Singly LL         | Circular LL          |
# +--------------------+-------------------+----------------------+
# | Last node points   | None              | Head                 |
# | Traversal          | One-direction     | Cyclic               |
# | Loop risk          | Low               | High (if careless)   |
# | Use case           | General           | Round-robin tasks    |
# +--------------------+-------------------+----------------------+

# ============================================================
#              COMMON MISTAKES (VERY IMPORTANT)
# ============================================================

# 1. Forgetting to stop traversal (infinite loop)
# 2. Not updating last node correctly
# 3. Losing head reference
# 4. Improper deletion of head node

# ============================================================
#              THINKING TIP
# ============================================================

# Always stop traversal when:
# current.next == head OR current == head

# ============================================================
# End of File: 001 Circular_Linked_List.py
# ============================================================
