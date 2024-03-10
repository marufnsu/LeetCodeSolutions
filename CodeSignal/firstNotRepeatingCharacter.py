"""
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. 
If there is no such character, return '_'.

Example
For s = "abacabad", the output should be
solution(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
solution(s) = '_'.

There are no characters in this string that do not repeat.
"""

def solution(s):
    unique = {}
    for ch in s:
        if unique.get(ch):
            unique[ch] += 1
        else:
            unique[ch] = 1
    for key in unique:
        if unique[key] == 1:
            return key
    return '_'

"""
def solution(s):
    for c in s:
        if s.index(c) == s.rindex(c):
            return c
    return '_'
"""