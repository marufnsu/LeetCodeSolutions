'''
443. String Compression
Hint
Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
Note that group lengths that are 10 or longer will be split into multiple characters in chars.
After you are done modifying the input array, return the new length of the array.
You must write an algorithm that uses only constant extra space.

Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
'''

class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        for i in range(len(chars)-1,-1,-1):
            if i and chars[i]==chars[i-1]:
                count += 1
                chars.pop(i)
            else:
                if count>1:
                    for item in str(count)[::-1]:
                        chars.insert(i+1, item)
                    count = 1


"""
class Solution:
    def compress(self, chars: List[str]) -> int:
        '''
        Two Pointers: O(N)
        1. 2 variables: cur char (res) and count
        2. loop through to update res and chars
        '''
        n = len(chars) 
        if n==1:
            return 1
        
        count = 1
        result = 0

        # O(N+1)
        for idx in range(1, n + 1):
            if idx < n and chars[idx-1] == chars[idx]:
                count += 1
                continue
            
            chars[result] = chars[idx - 1]
            result += 1

            if count > 1:
                s = str(count)
                m = len(s)
                chars[result:result + m] = s
                result += m
        
            count = 1

        return result
"""