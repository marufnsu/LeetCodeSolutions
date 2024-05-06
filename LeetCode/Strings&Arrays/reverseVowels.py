'''
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1
        vowelsList = "aeiouAEIOU"

        while left < right:
            if s[left] in vowelsList and s[right] in vowelsList:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] not in vowelsList:
                left += 1
            elif s[right] not in vowelsList:
                right -= 1
        return ''.join(s)
    
    '''
    class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = re.findall('[aeiouAEIOU]', s)
        return re.sub('[aeiouAEIOU]', lambda _ : vowels.pop(), s)
    '''