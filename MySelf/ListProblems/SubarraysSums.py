def find_subarrays_brute_force(arr, target_sum):
    result = []
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            if current_sum == target_sum:
                result.append(arr[i:j+1])  # Append the subarray
    return result

# Example usage
array = [1, 2, 3, 4, 5]
target = 5
print("Subarrays with sum =", target, ":", find_subarrays_brute_force(array, target))



def max_subarray_sum(arr):
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Example
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6
