# Problem: Find the last occurrence of a given number in a sorted array.

# This function finds the last occurrence of a given target in a sorted array using a modified binary search.


def last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Move right to find the last occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

# Example
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
print(last_occurrence(arr, target))  # Output: 3




# Time Complexity (Big-O Notation)
#   Worst case: 𝑂(log𝑛) (binary search reduces search space by half in each iteration).
#   Best case: 𝑂(1) (target found at the first mid check).
#   Average case: 𝑂(log𝑛).
# Space Complexity
#   Uses only integer variables (left, right, mid, result).
#   No extra space is used → O(1) (constant space).