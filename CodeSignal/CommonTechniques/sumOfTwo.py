"""
You have two integer arrays, a and b, and an integer target value v. Determine whether there is a pair of numbers, 
where one number is taken from a and the other from b, that can be added together to get a sum of v. Return true if such a pair exists, otherwise return false.

Example

For a = [1, 2, 3], b = [10, 20, 30, 40], and v = 42, the output should be
solution(a, b, v) = true.
"""

def solution(a, b, v):
    #No need to iterate a huge list, if the other list is empty
    if not a or not b:
        return False
    
    #kill duplicates
    b = set(b)
    
    #iterate through list a to look if the wanted difference is in b
    for x in a:
        if (v-x) in b:
            return True
    return False