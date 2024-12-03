# Here’s a Python solution to find the maximum and minimum elements in an array:

def find_max_and_min(arr):
    if not arr:  # Check if the array is empty
        return None, None  # Return None for both max and min

    # Initialize max and min with the first element of the array
    max_element = arr[0]
    min_element = arr[0]

    # Iterate through the array
    for num in arr:
        if num > max_element:
            max_element = num
        if num < min_element:
            min_element = num

    return max_element, min_element

# Example usage
array = [3, 1, 5, 7, 2, 8, 4]
maximum, minimum = find_max_and_min(array)
print("Maximum:", maximum)
print("Minimum:", minimum)
