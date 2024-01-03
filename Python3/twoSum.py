'''
Two Sum:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        nList = len(nums)

        for i in range(nList):
            compliment = target - nums[i]

            if compliment in numMap:
                return [numMap[compliment], i]
            numMap[nums[i]] = i

        return []


'''
More Solution:
def twoSum(self, nums: List[int], target: int) -> List[int]:
    numMap = {}
        
    for i, num in enumerate(nums):
        if target - num in numMap:
            return [numMap[target - num], i]           
        numMap[num] = i
'''