def rotate_right_naive(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k > n
    for _ in range(k):
        last = arr.pop()  # Remove last element
        arr.insert(0, last)  # Insert it at the beginning
    return arr

# Example usage
array = [1, 2, 3, 4, 5]
k = 3
print("Right Rotated Array:", rotate_right_naive(array, k))


def rotate_left_naive(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k > n
    for _ in range(k):
        first = arr.pop(0)  # Remove first element
        arr.append(first)  # Append it to the end
    return arr

# Example usage
array = [1, 2, 3, 4, 5]
k = 2
print("Left Rotated Array:", rotate_left_naive(array, k))


k=2
k = k % 5
print(k)


def rotate_array(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

# Example
print(rotate_array([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]
