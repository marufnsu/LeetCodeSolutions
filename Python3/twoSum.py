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

        for num in range(nList):
            compliment = target - nums[num]

            if compliment in numMap:
                return [numMap[compliment], num]
            numMap[nums[num]] = num

        return []


'''
More Solution:
def twoSum(self, nums: List[int], target: int) -> List[int]:
    numMap = {}
        
    for i, x in enumerate(nums):
        if target - x in numMap:
            return [numMap[target-x], i]           
        numMap[x] = i
'''