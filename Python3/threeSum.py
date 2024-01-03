'''
3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        result = set()

        #1. Split nums into three lists: negative numbers, positive numbers, and zeros
        negatives, positives = [], []
        zeroes = 0
        for num in nums:
            if num > 0:
                positives.append(num)
            elif num < 0: 
                negatives.append(num)
            else:
                zeroes += 1
        # 2. Create a separate set for negatives and positives for O(1) look-up times
        Neg, Pos = set(negatives), set(positives)

        # 3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if zeroes:
            for num in Pos:
                if -1 * num in Neg:
                    result.add((-1 * num, 0, num))

            # 3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
            if zeroes >= 3:
                result.add((0, 0, 0))

            # 4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
            #   exists in the positive number set
        from itertools import combinations

        for x, y in combinations(negatives, 2):
            target = -1 * (x + y)
            if target in Pos:
                result.add(tuple(sorted([x, y, target])))

        # 5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set

        for x, y in combinations(positives, 2):
            target = -1 * (x + y)
            if target in Neg:
                result.add(tuple(sorted([x, y, target])))

        return [list(x) for x in result]


'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            target = 0 - nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return list(result)
'''