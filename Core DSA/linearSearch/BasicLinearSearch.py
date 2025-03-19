# Problem: Given an array and a target value, return the index of the target if it exists; otherwise, return -1.


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example
arr = [4, 2, 7, 1, 9, 3]
target = 7
print(linear_search(arr, target))  # Output: 2
