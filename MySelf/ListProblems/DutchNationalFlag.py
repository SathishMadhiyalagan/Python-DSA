# Solution Using Dutch National Flag Algorithm

def sort_012(arr):
    low = 0       # Pointer for 0s
    mid = 0       # Pointer for 1s
    high = len(arr) - 1  # Pointer for 2s

    while mid <= high:
        if arr[mid] == 0:
            # Swap arr[low] and arr[mid], increment both
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            # No swap, just move mid forward
            mid += 1
        else:  # arr[mid] == 2
            # Swap arr[mid] and arr[high], decrement high
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

# Example usage
array = [1,0,1, 2, 1, 0, 2, 1,2,1,2,1, 0]
sorted_array = sort_012(array)
print("Sorted Array:", sorted_array)
