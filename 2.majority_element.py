# Given an array nums of size n, return the element that appears more than ⌊n/2⌋ times. You may assume the majority element always exists.

# Input:

# nums = [2, 2, 1, 1, 1, 2, 2]

 

# Output:

# 2

# Using hashmpa 
# Space Complexity O(n) 
# time complexity O(n)
def majority_element(nums):
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1
    expected_threshold = len(nums) // 2
    for number, count in freq_map.items():
        if count > expected_threshold:
            return number
    
    return - 1

# Using O(1) Space Complexity as Expected
# using O(n) time complexity
def majority_element_optimal(nums):
    majority = None
    count = 0
    for num in nums:
        if count == 0:
            majority = num
        if num == majority:
            count += 1
        else:
            count = -1
    return majority
    
print(majority_element_optimal([2,2,1,1,1,2,2]))