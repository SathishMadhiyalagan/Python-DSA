def generate_subarrays(arr):
    subarrays = []
    for i in range(len(arr)):  # Start index of subarray
        for j in range(i, len(arr)):  # End index of subarray (inclusive)
            subarrays.append(arr[i:j + 1])  # Append the subarray
    return subarrays

# Example usage
arr = ['p', 'w', 'w', 'k', 'e', 'w']
result = generate_subarrays(arr)
print(result)
