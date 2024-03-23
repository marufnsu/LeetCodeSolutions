"""
Given a sorted integer array that does not contain any duplicates, return a summary of the number ranges it contains.

Example

For nums = [-1, 0, 1, 2, 6, 7, 9], the output should be
solution(nums) = ["-1->2", "6->7", "9"].
"""

def solution(nums):
    # Initialize an empty list to store the summary of number ranges
    ranges = []
    
    # Continue the loop until the nums list is empty
    while nums:
        # Pop the first element from the nums list and use it as the start of the range
        start = end = nums.pop(0)
        
        # Continue extending the current range as long as there are more elements in nums
        # and the next element is consecutive to the current end
        while nums and nums[0] - end == 1:
            end = nums.pop(0)
        
        # Add the current range to the summary list
        # If the range has only one number, add it as a single string
        # Otherwise, add it in the format "start->end"
        ranges.append(str(start) + ('', '->' + str(end))[start != end])
    
    return ranges