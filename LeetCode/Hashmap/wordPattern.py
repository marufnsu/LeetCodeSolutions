'''
290. Word Pattern
Easy

Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lWords = s.split()
        if len(pattern) != len(lWords):
            return False
        cToW, wToC = {}, {}
        for c,w in zip(pattern, lWords):
            if (c in cToW and cToW[c] != w):
                return False
            if (w in wToC and wToC[w] != c):
                return False
            cToW[c] = w
            wToC[w] = c
        return True