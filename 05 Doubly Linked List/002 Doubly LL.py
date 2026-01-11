# ============================================================
#              DOUBLY LINKED LIST – BASICS (PYTHON)
# ============================================================

# A Doubly Linked List (DLL) is a linear data structure
# where each node contains:
# 1. Data
# 2. Reference to NEXT node
# 3. Reference to PREVIOUS node

# ============================================================
#              WHY DOUBLY LINKED LIST?
# ============================================================

# Singly Linked List:
# ❌ Can move only forward

# Doubly Linked List:
# ✅ Can move forward
# ✅ Can move backward
# ✅ Easier deletion (no need to track prev manually)

# Trade-off:
# ❌ Extra memory (prev pointer)

# ============================================================
#              NODE STRUCTURE
# ============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None    # Pointer to previous node
        self.next = None    # Pointer to next node

# ============================================================
#              DOUBLY LINKED LIST CLASS
# ============================================================

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # ========================================================
    #              INSERT AT END
    # ========================================================

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # ========================================================
    #              INSERT AT BEGINNING
    # ========================================================

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head:
            new_node.next = self.head
            self.head.prev = new_node

        self.head = new_node

    # ========================================================
    #              DELETE A NODE (BY VALUE)
    # ========================================================

    def delete(self, key):
        temp = self.head

        # Case 1: Empty list
        if temp is None:
            return

        # Case 2: Head node
        if temp.data == key:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        # Case 3: Middle or last node
        while temp and temp.data != key:
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        if temp.next:
            temp.next.prev = temp.prev

        if temp.prev:
            temp.prev.next = temp.next

    # ========================================================
    #              TRAVERSE FORWARD
    # ========================================================

    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    # ========================================================
    #              TRAVERSE BACKWARD
    # ========================================================

    def display_backward(self):
        temp = self.head

        if temp is None:
            return

        # Go to last node
        while temp.next:
            temp = temp.next

        # Traverse backward
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

    # ========================================================
    #              SEARCH ELEMENT
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


# ============================================================
#              TESTING DOUBLY LINKED LIST
# ============================================================

dll = DoublyLinkedList()

dll.append(10)
dll.append(20)
dll.append(30)

dll.insert_at_beginning(5)

print("Forward Traversal:")
dll.display_forward()

print("Backward Traversal:")
dll.display_backward()

print("Search 20:", dll.search(20))

dll.delete(20)
dll.display_forward()

# ============================================================
#              TIME COMPLEXITY
# ============================================================

# Access/Search → O(n)
# Insert head   → O(1)
# Insert tail   → O(n)
# Delete        → O(n)

# ============================================================
#              SINGLY vs DOUBLY LINKED LIST
# ============================================================

# +---------------------+------------------+------------------+
# | Feature             | Singly LL        | Doubly LL        |
# +---------------------+------------------+------------------+
# | Pointers            | next             | prev + next      |
# | Traversal           | One direction    | Both directions  |
# | Memory              | Less             | More             |
# | Deletion            | Harder           | Easier           |
# +---------------------+------------------+------------------+

# ============================================================
#              COMMON MISTAKES
# ============================================================

# 1. Forgetting to update prev pointer
# 2. Breaking links accidentally
# 3. Not handling head deletion properly
# 4. Losing reference to nodes

# ============================================================
#              THINKING TIPS
# ============================================================

# Always visualize:
# None <- [prev | data | next] <-> [prev | data | next] -> None

# ============================================================
# End of File: 044 Doubly_Linked_List.py
# ============================================================
