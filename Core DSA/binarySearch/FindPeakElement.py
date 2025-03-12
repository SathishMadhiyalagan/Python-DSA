# Problem: A peak element is an element that is strictly greater than its neighbors. Find the index of a peak element.


def find_peak(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left

# Example
arr = [1, 2, 3, 4,1]
print(find_peak(arr))  # Output: 2
