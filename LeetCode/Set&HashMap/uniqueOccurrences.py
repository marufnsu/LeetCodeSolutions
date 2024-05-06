'''
1207. Unique Number of Occurrences
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
'''

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        # enter elements into hashmap with their frequency
        for num in arr:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
    
        return len(freq) == len(set(freq.values()))