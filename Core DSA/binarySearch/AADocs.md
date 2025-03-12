Binary Search is an efficient searching algorithm used on sorted arrays. Below are multiple problems you can solve using **Binary Search** in Python:

---

### **1. Basic Binary Search**
#### **Problem:** Given a sorted array and a target value, return the index of the target if it exists; otherwise, return `-1`.
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example
arr = [1, 3, 5, 7, 9, 11]
target = 7
print(binary_search(arr, target))  # Output: 3
```

---

### **2. First Occurrence in a Sorted Array**
#### **Problem:** Find the first occurrence of a given number in a sorted array.
```python
def first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Move left to find the first occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

# Example
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
print(first_occurrence(arr, target))  # Output: 1
```

---

### **3. Last Occurrence in a Sorted Array**
#### **Problem:** Find the last occurrence of a given number in a sorted array.
```python
def last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Move right to find the last occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

# Example
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
print(last_occurrence(arr, target))  # Output: 3
```

---

### **4. Count Occurrences of a Number**
#### **Problem:** Given a sorted array, find the number of occurrences of a given element.
```python
def count_occurrences(arr, target):
    first = first_occurrence(arr, target)
    if first == -1:
        return 0
    last = last_occurrence(arr, target)
    return last - first + 1

# Example
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
print(count_occurrences(arr, target))  # Output: 3
```

---

### **5. Find the Square Root using Binary Search**
#### **Problem:** Given a number `x`, find the square root of `x` rounded down to the nearest integer.
```python
def sqrt_binary_search(x):
    if x < 2:
        return x
    left, right = 1, x // 2
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
            ans = mid  # Store possible answer
        else:
            right = mid - 1
    return ans

# Example
print(sqrt_binary_search(25))  # Output: 5
print(sqrt_binary_search(10))  # Output: 3
```

---

### **6. Search in a Rotated Sorted Array**
#### **Problem:** Given a rotated sorted array, find a target element’s index.
```python
def search_rotated(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:  # Left half is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

# Example
arr = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search_rotated(arr, target))  # Output: 4
```

---

### **7. Find Peak Element**
#### **Problem:** A peak element is an element that is strictly greater than its neighbors. Find the index of a peak element.
```python
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
arr = [1, 2, 3, 1]
print(find_peak(arr))  # Output: 2
```

---

### **8. Find Minimum in Rotated Sorted Array**
#### **Problem:** Find the minimum element in a rotated sorted array.
```python
def find_min(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[right]:  
            left = mid + 1  
        else:
            right = mid
    return arr[left]

# Example
arr = [3, 4, 5, 1, 2]
print(find_min(arr))  # Output: 1
```

---

### **9. Find Position to Insert in Sorted Array (Lower Bound)**
#### **Problem:** Find the index where an element should be inserted in a sorted array to keep it sorted.
```python
def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

# Example
arr = [1, 3, 5, 6]
target = 5
print(lower_bound(arr, target))  # Output: 2
```

---

### **10. Find the Smallest Missing Positive Number**
#### **Problem:** Given a sorted array of unique positive integers, find the smallest missing positive number.
```python
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
```

---