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
    # Create a dictionary to store the count of each character in the string
    unique = {}
    
    # Iterate through each character in the string
    for ch in s:
        # If the character is already in the dictionary, increment its count
        if unique.get(ch):
            unique[ch] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            unique[ch] = 1
    
    # Iterate through each character and its count in the dictionary
    for key in unique:
        # If the count of a character is 1, return that character
        if unique[key] == 1:
            return key
    
    # If no character with count 1 is found, return '_'
    return '_'

"""
def solution(s):
    for c in s:
        if s.index(c) == s.index(c):
            return c
    return '_'
"""