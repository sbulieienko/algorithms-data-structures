"""
Given a non-empty list of integers, every element appears twice except for one. Find that single one.
"""

def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Example usage:
if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2, 4, 5]
    print(single_number(nums))  # Output: 5 
# The function uses the XOR bitwise operation to find the single number.  Since x ^ x = 0 and x ^ 0 = x, all duplicate numbers cancel each other out, leaving only the single number.