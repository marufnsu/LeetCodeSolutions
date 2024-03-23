"""
You have two strings, s and t. The string t contains only unique elements. 
Find and return the minimum consecutive substring of s that contains all of the elements from t.

It's guaranteed that the answer exists. If there are several answers, return the one which starts from the smallest index.

Example

For s = "adobecodebanc" and t = "abc", the output should be
solution(s, t) = "banc".
"""
def solution(s, t):
    # Iterate over all possible lengths of substrings of s
    for x in range(len(s)+1):
        # Iterate over all possible starting positions of substrings of length x in s
        for p in range(len(s)-x+1):
            # Filter characters in the current substring (p:p+x) that are also in t
            c = filter(lambda x: x in t, s[p:p+x])
            # Check if the filtered characters form all characters in t
            if len(set(c)) == len(t):
                # If yes, return the substring
                return s[p:p+x]
    # If no substring is found, return an empty string
    return ""

"""
Explanation:

The outer loop iterates over all possible lengths of substrings of string s.
The inner loop iterates over all possible starting positions of substrings of the current length in string s.
The filter function is used to extract characters from the current substring s[p:p+x] that are also present in string t.
The filtered characters are stored in the variable c.
The code checks if the set of filtered characters c contains all characters from string t. If it does, it means the substring s[p:p+x] contains all characters from t.
If such a substring is found, it is returned. If not, an empty string is returned.
"""