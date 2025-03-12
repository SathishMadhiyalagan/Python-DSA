# Problem: Given a sorted array of unique positive integers, find the smallest missing positive number.

def find_missing(arr):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] == mid + 1:
            left = mid + 1
        else:
            right = mid
    return left + 1

# Example
arr = [1, 2, 3, 5, 6]
print(find_missing(arr))  # Output: 4
