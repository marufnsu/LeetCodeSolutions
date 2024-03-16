"""
Given an array of integers nums and an integer k, determine whether there are two distinct indices i and j in the array 
where nums[i] = nums[j] and the absolute difference between i and j is less than or equal to k.

Example
For nums = [0, 1, 2, 3, 5, 2] and k = 3, the output should be
solution(nums, k) = true.

There are two 2s in nums, and the absolute difference between their positions is exactly 3.

For nums = [0, 1, 2, 3, 5, 2] and k = 2, the output should be
solution(nums, k) = false.

The absolute difference between the positions of the two 2s is 3, which is more than k.
"""

def solution(nums, k):
    indices = {}  # Dictionary to store indices of previously encountered numbers
    
    # Iterate through the nums array along with its indices
    for i, num in enumerate(nums):
        # If the current number has been seen before and the absolute difference
        # between the current index and the index of the previous occurrence is less than or equal to k
        if num in indices and i - indices[num] <= k:
            return True  # Found a pair with the required condition, return True
        indices[num] = i  # Update the index of the current number in the dictionary
    
    # If no such pair is found during the iteration, return False
    return False