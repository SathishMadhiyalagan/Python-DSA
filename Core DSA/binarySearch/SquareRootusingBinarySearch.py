# Problem: Given a number x, find the square root of x rounded down to the nearest integer.

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


