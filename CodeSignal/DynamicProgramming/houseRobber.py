"""
You are planning to rob houses on a specific street, and you know that every house on the street has a certain amount of money hidden. 
The only thing stopping you from robbing all of them in one night is that adjacent houses on the street have a connected security system. 
The system will automatically trigger an alarm if two adjacent houses are broken into on the same night.

Given a list of non-negative integers nums representing the amount of money hidden in each house, 
determine the maximum amount of money you can rob in one night without triggering an alarm.

Example

For nums = [1, 1, 1], the output should be
solution(nums) = 2.

The optimal way to get the most money in one night is to rob the first and the third houses for a total of 2.
"""

def solution(nums):
    # Get the number of houses
    n = len(nums)
    
    # Base cases:
    # If there are no houses, return 0
    if n == 0:
        return 0
    # If there is only one house, return its value
    if n == 1:
        return nums[0]
    
    # Initialize an array to store the maximum amount of money we can rob up to each house
    dp = [0] * n
    
    # Initialize the first two elements of the dp array
    dp[0] = nums[0]  # Maximum amount of money we can rob up to the first house
    dp[1] = max(nums[0], nums[1])  # Maximum amount of money we can rob up to the second house
    
    # Iterate through the remaining houses starting from the third house
    for i in range(2, n):
        # For each house i, the maximum amount of money we can rob is the maximum of two options:
        # 1. Rob the current house (nums[i]) plus the maximum amount of money we could rob up to two houses before (dp[i-2])
        # 2. Skip the current house and take the maximum amount of money we could rob up to the previous house (dp[i-1])
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])
    
    # Return the maximum amount of money we can rob without triggering an alarm, which is dp[n-1]
    return dp[n-1]

"""
def solution(A):
    # Initialize two variables to keep track of the maximum sums:
    # a represents the maximum sum that includes the current element x
    # b represents the maximum sum that excludes the current element x
    a = b = 0
    
    # Iterate through each element x in the array A
    for x in A:
        # Calculate the new value of a:
        # Include the current element x and add it to the maximum sum without the previous element (b)
        a, b = b + x, max(a, b)
    
    # Return the maximum of the two sums: a and b
    # This represents the maximum sum that can be obtained from the entire array A
    return max(a, b)
"""