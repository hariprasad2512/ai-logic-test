# Q4. Container with Most Water

# Given an array height where each element is the height of a vertical line at that index, find two lines that together with the x-axis form a container holding the most water. Return that maximum area.

# Input:

# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# Output:

# 49

# ●       Target O(n) time using the two-pointer technique.

# ●       Explain your approach and complexity.

# Two Pointer approach
# Time Complexity - O(N)
# Space Complexity - O(1)
def container_with_most_water(height):
    left = 0
    right = len(height) - 1
    max_water = 0
    
    while left < right:
        current_height = min(height[left], height[right])
        current_width = right - left
        area = current_height * current_width
        max_water = max(max_water , area)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_water

print(container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))