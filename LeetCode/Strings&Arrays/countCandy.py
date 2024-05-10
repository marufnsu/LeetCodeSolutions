'''
135. Candy
Hard

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.


Example 1:
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
'''

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        tCandy = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                tCandy[i] = tCandy[i - 1] + 1
        
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                tCandy[i] = max(tCandy[i], tCandy[i + 1] + 1)
        
        return sum(tCandy)
    
    '''
    Alternative Solution:
    class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        
        ret, up, down, peak = 1, 0, 0, 0
        
        for prev, curr in zip(ratings[:-1], ratings[1:]):
            if prev < curr:
                up, down, peak = up + 1, 0, up + 1
                ret += 1 + up
            elif prev == curr:
                up = down = peak = 0
                ret += 1
            else:
                up, down = 0, down + 1
                ret += 1 + down - int(peak >= down)
        
        return ret    
    '''