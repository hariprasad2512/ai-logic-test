# Given an array nums of size n, return the element that appears more than ⌊n/2⌋ times. You may assume the majority element always exists.

# Input:

# nums = [2, 2, 1, 1, 1, 2, 2]

 

# Output:

# 2
def majority_element(nums):
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1
    expected_threshold = len(nums) // 2
    for number, count in freq_map.items():
        if count > expected_threshold:
            return number
    
    return - 1
    
print(majority_element([2,2,1,1,1,2,2]))