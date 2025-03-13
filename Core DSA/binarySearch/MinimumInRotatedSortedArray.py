# Problem: Find the minimum element in a rotated sorted array.


def find_min(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[right]:  
            left = mid + 1  
        else:
            right = mid
    return arr[left]

# Example
arr = [3, 4, 5, 1, 2]
print(find_min(arr))  # Output: 1
