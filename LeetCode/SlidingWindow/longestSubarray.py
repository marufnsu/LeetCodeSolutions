'''
1493. Longest Subarray of 1's After Deleting One Element
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. 
Return 0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
'''

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        k = 1
        if 0 not in nums:
                return len(nums) - 1
        for end in range(len(nums)):
            if nums[end] == 0:
                k -= 1
            if k < 0:
                if nums[start] == 0:
                    k += 1
                start += 1
        return end - start