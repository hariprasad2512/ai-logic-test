# Given an integer array nums and an integer target, return the indices of the two numbers that add up to target. You may assume exactly one solution exists and you may not use the same element twice.

# Input:

# nums = [2, 7, 11, 15], target = 9
# Output:

# [0, 1]
def two_sum(nums, target):
    num_to_index = {}
    for i in range(len(nums)):
        num_to_index[nums[i]] = i
    
    for i in range(len(nums)):
        current = nums[i]
        complement = target - nums[i]
        if complement in num_to_index:
            return i, num_to_index[complement]
        num_to_index[current] = i 
    return -1

print(two_sum([2,7, 11, 15], 9))