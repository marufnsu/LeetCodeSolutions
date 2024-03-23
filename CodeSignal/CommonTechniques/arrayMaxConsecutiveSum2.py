"""
Given an array of integers, find the maximum possible sum you can get from one of its contiguous subarrays. 
The subarray from which this sum comes must contain at least 1 element.

Example
For inputArray = [-2, 2, 5, -11, 6], the output should be
solution(inputArray) = 7.

The contiguous subarray that gives the maximum possible sum is [2, 5], with a sum of 7.
"""

def solution(inputArray):
    max_sum = float('-inf')  # Initialize maximum sum with negative infinity
    
    current_sum = 0  # Initialize current sum
    
    # Iterate through the array
    for num in inputArray:
        # Update current sum by adding the current number
        current_sum += num
        # Update max_sum if current_sum exceeds it
        max_sum = max(max_sum, current_sum)
        # Reset current_sum to 0 if it becomes negative (to start a new subarray)
        current_sum = max(0, current_sum)
    
    return max_sum  # Return the maximum sum found

"""
Explanation:

Initialize max_sum with negative infinity to handle cases where all elements in the array are negative.
Initialize current_sum to 0 to start calculating the sum of the current contiguous subarray.
Iterate through the array:
    Update current_sum by adding the current number to it.
    Update max_sum if current_sum exceeds it.
    Reset current_sum to 0 if it becomes negative, indicating the start of a new subarray.
After iterating through the array, return the max_sum found, which represents the maximum possible sum of a contiguous subarray.
"""