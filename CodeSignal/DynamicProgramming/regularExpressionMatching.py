"""
Note: Avoid using regular expressions and implement regex matching yourself in your solution, 
since this is what you would be asked to do during a real interview.

Implement regular expression matching with support for '.' and '*', given the following guidelines:
'.' Matches any single character.
'*' Matches zero or more of the element that comes before it.

The matching should cover the entire input string s. If the pattern p matches the input string s, return true, otherwise return false.

Example
For s = "bb" and p = "b", the output should be
solution(s, p) = false;
For s = "zab" and p = "z.*", the output should be
solution(s, p) = true;
For s = "caab" and p = "d*c*x*a*b", the output should be
solution(s, p) = true.
"""

def solution(s, p):
    # Base cases
    if not p:
        return not s
    if len(p) == 1:
        return len(s) == 1 and (s[0] == p[0] or p[0] == '.')

    # Check for '*'
    if p[1] == '*':
        # Case 1: Ignore '*' and its preceding character
        if solution(s, p[2:]):
            return True
        # Case 2: Match '*' and its preceding character with current character in s
        return bool(s) and (s[0] == p[0] or p[0] == '.') and solution(s[1:], p)
    
    # Check for '.' or matching characters
    if s and (s[0] == p[0] or p[0] == '.'):
        return solution(s[1:], p[1:])
    
    return False

"""
Here's a step-by-step explanation of the algorithm:

If the pattern p is empty, return True if the input string s is also empty; otherwise, return False.
If the pattern p has a length of 1, check if the input string s also has a length of 1 and if they match or if the pattern p is '.'. Return True if either condition is met; otherwise, return False.
If the second character of the pattern p is '*', recursively call the function with two possible scenarios:
Ignore the '*' and its preceding character in the pattern p.
Match the '*' and its preceding character in the pattern p with the current character in the input string s.
If the second character of the pattern p is not '*', compare the first characters of both p and s. If they match or if the pattern p is '.', recursively call the function with the next characters of both p and s.
Return the result of the recursive calls.
"""