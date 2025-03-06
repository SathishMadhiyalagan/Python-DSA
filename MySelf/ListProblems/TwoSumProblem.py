# Given an array of integers, find two numbers such that they add up to a specific target number.


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

nums = [2, 5,7, 11, 15,4]

target = 9

print(two_sum(nums,target))