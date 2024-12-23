# Reverse the array

def reverse_array_recursive(arr, left, right):
    if left >= right:
        return

    # Swap elements
    arr[left], arr[right] = arr[right], arr[left]
    reverse_array_recursive(arr, left + 1, right - 1)

# Example usage
array = [1, 2, 3,6, 4, 5]

reverse_array_recursive(array, 0, len(array) - 1)

print("Reversed Array:", array)


