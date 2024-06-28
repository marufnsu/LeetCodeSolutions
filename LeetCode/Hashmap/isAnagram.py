'''
242. Valid Anagram

Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        isAnag = {}
        for c in s:
            if c not in isAnag:
                isAnag[c] = 1
            else:
                isAnag[c] += 1
        for c in t:
            if c in isAnag and isAnag[c] != 0:
                isAnag[c] -= 1
            else:
                return False
        return True