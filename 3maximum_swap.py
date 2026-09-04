# Q3. Maximum Swap

# Given a non-negative integer num, you may swap two digits at most once to get the maximum valued number. Return the maximum valued number you can get.

# Input:

# num = 2736

 

# Output:

# 7236

# ●       Consider edge cases (already-maximal numbers, repeated digits).

# ●       Explain your approach and complexity.


# Swap the first left digit with the largest Right Digit
def maximum_swap(num):
    digits = list(str(num))
    last_position = {}

    for index, digit in enumerate(digits):
        last_position[digit] = index
    
    for i, digit in enumerate(digits):
        for digit in range(9, int(digit), -1):
            
            j = last_position.get(str(digit))
            
            if j is not None and j > i:
                # SWAP the largest available digit from the Right
                digits[i], digits[j] = (
                    digits[j],
                    digits[i],
                )
                return int("".join(digits))

    return num

print(maximum_swap(2736))

