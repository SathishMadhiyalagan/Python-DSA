Linear Search is a simple searching algorithm that checks each element in a list sequentially until the target value is found or the list ends. Below are **10 Linear Search problems** with Python solutions.

---

### **1. Basic Linear Search**

#### **Problem:** Given an array and a target value, return the index of the target if it exists; otherwise, return `-1`.
```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example
arr = [4, 2, 7, 1, 9, 3]
target = 7
print(linear_search(arr, target))  # Output: 2
```

---

### **2. Find First Occurrence**
#### **Problem:** Find the first occurrence of a target element in an array.
```python
def first_occurrence(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example
arr = [1, 2, 2, 3, 4, 2, 5]
target = 2
print(first_occurrence(arr, target))  # Output: 1
```

---

### **3. Find Last Occurrence**
#### **Problem:** Find the last occurrence of a target element in an array.
```python
def last_occurrence(arr, target):
    index = -1
    for i in range(len(arr)):
        if arr[i] == target:
            index = i
    return index

# Example
arr = [1, 2, 2, 3, 4, 2, 5]
target = 2
print(last_occurrence(arr, target))  # Output: 5
```

---

### **4. Count Occurrences**
#### **Problem:** Count the number of times a target element appears in an array.
```python
def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count

# Example
arr = [1, 2, 2, 3, 4, 2, 5]
target = 2
print(count_occurrences(arr, target))  # Output: 3
```

---

### **5. Find the Maximum Element**
#### **Problem:** Find the maximum element in an array using linear search.
```python
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# Example
arr = [4, 7, 1, 9, 3]
print(find_max(arr))  # Output: 9
```

---

### **6. Find the Minimum Element**
#### **Problem:** Find the minimum element in an array using linear search.
```python
def find_min(arr):
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val

# Example
arr = [4, 7, 1, 9, 3]
print(find_min(arr))  # Output: 1
```

---

### **7. Find an Element in a 2D Array**
#### **Problem:** Given a 2D array and a target, find if the target exists.
```python
def search_2d(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return (i, j)  # Return the position as (row, column)
    return -1

# Example
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
target = 5
print(search_2d(matrix, target))  # Output: (1, 1)
```

---

### **8. Check if an Array is Sorted**
#### **Problem:** Check if an array is sorted in ascending order.
```python
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# Example
arr = [1, 2, 3, 4, 5]
print(is_sorted(arr))  # Output: True
```

---

### **9. Find the Missing Number in a Consecutive Sequence**
#### **Problem:** Given an array of `n` numbers from `1` to `n+1` with one number missing, find the missing number.
```python
def find_missing(arr, n):
    for i in range(1, n + 2):
        if i not in arr:
            return i

# Example
arr = [1, 2, 4, 5, 6]
n = 5
print(find_missing(arr, n))  # Output: 3
```

---

### **10. Find the Second Largest Element**
#### **Problem:** Find the second largest element in an array using linear search.
```python
def second_largest(arr):
    if len(arr) < 2:
        return None
    first, second = float('-inf'), float('-inf')
    for num in arr:
        if num > first:
            second, first = first, num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None

# Example
arr = [10, 20, 4, 45, 99, 99]
print(second_largest(arr))  # Output: 45
```

---
