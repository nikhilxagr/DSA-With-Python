# ============================================================
#                    ARRAYS IN PYTHON
# ============================================================

# In Python, arrays are usually implemented using:
# 1. List (MOST COMMON)
# 2. array module (rare in DSA)
# 3. numpy arrays (advanced, scientific)

# For DSA → ALWAYS use Python LIST

# ============================================================
#                    WHAT IS AN ARRAY?
# ============================================================

# An array is a collection of elements
# stored at CONTIGUOUS memory locations (conceptually)

# Key properties:
# - Same type of data (conceptually)
# - Indexed
# - Fixed order

# ============================================================
#                    ARRAY CREATION
# ============================================================

arr = [10, 20, 30, 40, 50]
print(arr)

# ============================================================
#                    ARRAY INDEXING
# ============================================================

print(arr[0])     # First element
print(arr[-1])    # Last element

# ============================================================
#                    ARRAY TRAVERSAL
# ============================================================

# Using for loop
for x in arr:
    print(x)

# Using index
for i in range(len(arr)):
    print(i, arr[i])

# ============================================================
#                    ARRAY INSERTION
# ============================================================

arr.append(60)        # Add at end → O(1)
arr.insert(2, 25)     # Insert at index → O(n)
print(arr)

# ============================================================
#                    ARRAY DELETION
# ============================================================

arr.pop()             # Remove last → O(1)
arr.pop(1)            # Remove by index → O(n)
arr.remove(30)        # Remove by value → O(n)
print(arr)

# ============================================================
#                    ARRAY SEARCHING
# ============================================================

# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search(arr, 40))

# Time Complexity → O(n)

# ============================================================
#                    ARRAY UPDATION
# ============================================================

arr[0] = 100
print(arr)

# ============================================================
#                    ARRAY SLICING
# ============================================================

print(arr[1:4])
print(arr[::-1])   # Reverse array

# ============================================================
#                    COMMON ARRAY OPERATIONS
# ============================================================

print(len(arr))      # Length
print(max(arr))      # Max element
print(min(arr))      # Min element
print(sum(arr))      # Sum of elements

# ============================================================
#                    ARRAY TIME COMPLEXITY
# ============================================================

# Access        → O(1)
# Search        → O(n)
# Insert end    → O(1)
# Insert middle → O(n)
# Delete end    → O(1)
# Delete middle → O(n)

# ============================================================
#                    IN-PLACE VS EXTRA SPACE
# ============================================================

# In-place → No extra array used
# Extra space → New array used

# In-place reverse
def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

reverse_array(arr)
print(arr)

# ============================================================
#                    IMPORTANT ARRAY PATTERNS
# ============================================================

# 1. Traversal
# 2. Two Pointer
# 3. Sliding Window
# 4. Prefix Sum
# 5. Sorting + Searching

# ============================================================
# End of File: 001 Arrays_Basics.py
# ============================================================
