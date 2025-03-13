# Problem: Find the index where an element should be inserted in a sorted array to keep it sorted.


def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

# Example
arr = [1, 3, 5, 6]
target = 5
print(lower_bound(arr, target))  # Output: 2
