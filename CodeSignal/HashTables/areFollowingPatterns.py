"""
Given an array strings, determine whether it follows the sequence given in the patterns array. In other words, 
there should be no i and j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j] or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].

Example
For strings = ["cat", "dog", "dog"] and patterns = ["a", "b", "b"], the output should be
solution(strings, patterns) = true;
For strings = ["cat", "dog", "doggy"] and patterns = ["a", "b", "b"], the output should be
solution(strings, patterns) = false.
"""

def solution(strings, patterns):
    # Create an empty dictionary to store mappings from patterns to strings
    d = {}
    
    # Iterate through each string-pattern pair
    for s, p in zip(strings, patterns):
        # If the pattern is already in the dictionary and its corresponding string is different,
        # return False since it violates the pattern
        if p in d and d[p] != s:
            return False
        # Update the mapping of pattern to string
        d[p] = s
    
    # Check if the number of unique values (strings) in the dictionary
    # is equal to the total number of key-value pairs in the dictionary
    # If not, it means there are duplicate strings for different patterns,
    # violating the pattern rule
    return len(d) == len(set(d.values()))

"""
def solution(strings, patterns):
    # Create two dictionaries to store mappings from strings to patterns and vice versa
    str_to_pat = {}
    pat_to_str = {}
    
    # Iterate through each string-pattern pair
    for s, p in zip(strings, patterns):
        # If the string is already mapped to a different pattern, return False
        if s in str_to_pat and str_to_pat[s] != p:
            return False
        # If the pattern is already mapped to a different string, return False
        if p in pat_to_str and pat_to_str[p] != s:
            return False
        # Update the mappings
        str_to_pat[s] = p
        pat_to_str[p] = s
    
    # If no conflicting mappings are found, return True
    return True
"""