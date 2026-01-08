# ============================================================
#                ARRAYS – DEEP DIVE (PYTHON)
# ============================================================

# Arrays are the FOUNDATION of DSA
# 80% of DSA problems are built on ARRAY PATTERNS

# Python uses LIST to represent arrays in DSA

# ============================================================
#                CORE ARRAY PROPERTIES
# ============================================================

# 1. Indexed (0-based)
# 2. Contiguous memory (conceptually)
# 3. Fast access
# 4. Slow insertion/deletion in middle
# 5. Mutable

# ============================================================
#                ARRAY MEMORY MODEL (IMPORTANT)
# ============================================================

# Index:   0    1    2    3
# Value:  10   20   30   40
# Memory: [ ][ ][ ][ ]

# Access by index → O(1)
# Because memory address = base + index * size

# ============================================================
#                ARRAY OPERATIONS & COMPLEXITY
# ============================================================

# Access        → O(1)
# Search        → O(n)
# Insert end    → O(1)
# Insert middle → O(n)
# Delete end    → O(1)
# Delete middle → O(n)

# ============================================================
#                BASIC ARRAY TEMPLATE
# ============================================================

arr = [3, 1, 4, 1, 5, 9, 2]

# ============================================================
#                ARRAY TRAVERSAL PATTERN
# ============================================================

def traverse(arr):
    for i in range(len(arr)):
        print(arr[i])

# ============================================================
#                LINEAR SEARCH (BASE OF ALL SEARCH)
# ============================================================

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Time → O(n)
# Space → O(1)

# ============================================================
#                FIND MAX & MIN (INTERVIEW FAVORITE)
# ============================================================

def find_max_min(arr):
    max_val = arr[0]
    min_val = arr[0]

    for x in arr:
        if x > max_val:
            max_val = x
        if x < min_val:
            min_val = x

    return max_val, min_val

# ============================================================
#                REVERSE ARRAY (IN-PLACE)
# ============================================================

def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

# Pattern → TWO POINTER
# Time → O(n)
# Space → O(1)

# ============================================================
#                CHECK IF ARRAY IS SORTED
# ============================================================

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# ============================================================
#                REMOVE DUPLICATES (SORTED ARRAY)
# ============================================================

def remove_duplicates(arr):
    if len(arr) == 0:
        return 0

    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return i + 1

# Pattern → TWO POINTER
# Time → O(n)
# Space → O(1)

# ============================================================
#                MOVE ZEROS TO END
# ============================================================

def move_zeros(arr):
    non_zero = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero], arr[i] = arr[i], arr[non_zero]
            non_zero += 1

# Pattern → TWO POINTER
# Time → O(n)

# ============================================================
#                ROTATE ARRAY BY 1 (RIGHT)
# ============================================================

def rotate_by_one(arr):
    last = arr[-1]

    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = last

# ============================================================
#                ROTATE ARRAY BY K (OPTIMAL)
# ============================================================

def rotate_by_k(arr, k):
    k = k % len(arr)

    arr.reverse()
    arr[:k] = reversed(arr[:k])
    arr[k:] = reversed(arr[k:])

# Pattern → REVERSE TECHNIQUE
# Time → O(n)
# Space → O(1)

# ============================================================
#                SECOND LARGEST ELEMENT
# ============================================================

def second_largest(arr):
    first = second = float('-inf')

    for x in arr:
        if x > first:
            second = first
            first = x
        elif x > second and x != first:
            second = x

    return second

# ============================================================
#                TWO SUM (VERY IMPORTANT)
# ============================================================

def two_sum(arr, target):
    seen = {}

    for i, num in enumerate(arr):
        diff = target - num
        if diff in seen:
            return seen[diff], i
        seen[num] = i

    return -1

# Pattern → HASHING
# Time → O(n)
# Space → O(n)

# ============================================================
#                MAJORITY ELEMENT (n/2 times)
# ============================================================

def majority_element(arr):
    count = 0
    candidate = None

    for num in arr:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate

# Pattern → BOYER-MOORE
# Time → O(n)
# Space → O(1)

# ============================================================
#                MAX SUBARRAY SUM (KADANE)
# ============================================================

def max_subarray(arr):
    max_sum = curr_sum = arr[0]

    for i in range(1, len(arr)):
        curr_sum = max(arr[i], curr_sum + arr[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum

# Pattern → DP + ARRAY
# Time → O(n)

# ============================================================
#                PREFIX SUM PATTERN
# ============================================================

def prefix_sum(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix

# ============================================================
#                SUBARRAY SUM EQUAL TO K
# ============================================================

def subarray_sum_k(arr, k):
    prefix_sum = 0
    seen = {0: 1}
    count = 0

    for num in arr:
        prefix_sum += num
        if prefix_sum - k in seen:
            count += seen[prefix_sum - k]
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

    return count

# Pattern → PREFIX SUM + HASHING
# Time → O(n)

# ============================================================
#                ARRAY PATTERN SUMMARY (MUST MEMORIZE)
# ============================================================

# 1. Traversal
# 2. Two Pointer
# 3. Sliding Window
# 4. Prefix Sum
# 5. Hashing
# 6. Sorting + Greedy
# 7. Kadane
# 8. Boyer-Moore

# ============================================================
#                INTERVIEW THINKING CHECKLIST
# ============================================================

# Ask before coding:
# 1. Sorted or unsorted?
# 2. Can I do in one pass?
# 3. Can I use two pointers?
# 4. Can I reduce space?
# 5. What is the brute force?

# ============================================================
# End of File: 031 Arrays_Deep_Dive.py
# ============================================================
