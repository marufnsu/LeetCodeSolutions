'''
Leetcode Question# 01
----------------------
Two Sum:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Possible Clarification Questions:
---------------------------------
- Does the array contain only positive or negative numbers?
- What if the same pair repeats twice, should we print it every time?
- If the reverse of the pair is acceptable e.g. can we print both (4, 1) and (1, 4) if the given sum is 5.
- Do we need to print only distinct pairs? Does (3, 3) is valid pair for given sum 0f 6?
- How big is the array?
''' 
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
            
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in seen:
                return [seen[compliment], i]           
            seen[num] = i
        return []