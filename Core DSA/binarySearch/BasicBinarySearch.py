# Problem: Given a sorted array and a target value, return the index of the target if it exists; otherwise, return -1.

# Binary search is an efficient searching algorithm used on a sorted array. It works by repeatedly dividing the search range in half until the target element is found or the range is empty.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example
arr = [1, 3, 5, 7, 9, 11]
target = 7
print(binary_search(arr, target))  # Output: 3


# Time Complexity Analysis (Big-O Notation)
#    - Each step reduces the search space by half.
#    - If the array length is 𝑛, the number of steps required is approximately log2(n)
#    - Best case: 𝑂(1)O(1) (if target is found at the first mid check).
#    - Worst case: O(logn) (when we keep halving until one element is left).
#    - Average case: O(logn).

# Space Complexity
#    - Uses only a few integer variables (left, right, mid).
#    - No extra data structures → O(1) (constant space).