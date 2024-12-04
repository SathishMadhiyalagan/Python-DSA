def kth_smallest(arr, k):
    arr.sort()  # Sort the array in ascending order
    print(arr)
    return arr[k - 1]  # Return the k-th smallest element

# Example usage
array = [7, 10, 4, 3, 20, 15]
k = 3
print("K-th Smallest Element:", kth_smallest(array, k))


def kth_largest(arr, k):
    arr.sort(reverse=True)  # Sort the array in descending order
    print(arr)
    return arr[k - 1]  # Return the k-th largest element

# Example usage
array = [7, 10, 4, 3, 20, 15]
k = 3
print("K-th Largest Element:", kth_largest(array, k))



def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, k):
    if low <= high:
        pi = partition(arr, low, high)
        if pi == k - 1:
            return arr[pi]
        elif pi > k - 1:
            return quickselect(arr, low, pi - 1, k)
        else:
            return quickselect(arr, pi + 1, high, k)

def kth_smallest(arr, k):
    return quickselect(arr, 0, len(arr) - 1, k)

# Example usage
array = [7, 10, 4, 3, 20, 15]
k = 3
print("K-th Smallest Element:", kth_smallest(array, k))


def kth_largest(arr, k):
    return quickselect(arr, 0, len(arr) - 1, len(arr) - k + 1)

# Example usage
array = [7, 10, 4, 3, 20, 15]
k = 3
print("K-th Largest Element:", kth_largest(array, k))

