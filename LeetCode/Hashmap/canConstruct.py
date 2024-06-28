'''
383. Ransom Note
Easy

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        canConst = {}

        for ltr in magazine:
            if ltr in canConst:
                canConst[ltr] += 1
            else:
                canConst[ltr] = 1
        
        for ltr in ransomNote:
            if ltr in canConst and canConst[ltr] > 0:
                canConst[ltr] -= 1
            else:
                return False
        return True