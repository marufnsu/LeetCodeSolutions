"""
DIFFICULTY LEVEL: HARD
You have two arrays of strings, words and parts. Return an array that contains the strings from words, 
modified so that any occurrences of the substrings from parts are surrounded by square brackets [], following these guidelines:

If several parts substrings occur in one string in words, choose the longest one. If there is still more than one such part, then choose the one that appears first in the string.

Example
For words = ["Apple", "Melon", "Orange", "Watermelon"] and parts = ["a", "mel", "lon", "el", "An"], the output should be
solution(words, parts) = ["Apple", "Me[lon]", "Or[a]nge", "Water[mel]on"].

While "Watermelon" contains three substrings from the parts array, "a", "mel", and "lon", "mel" is the longest substring that appears first in the string.
"""

def solution(words, parts):
    # Convert parts list to a set for efficient lookup
    parts = set(parts)
    # Initialize an empty list to store the modified words
    ans = []
    # Iterate through each word in the words array
    for s in words:
        # Start with the maximum possible length of the part substring
        length = 5
        # Iterate from maximum to minimum length to find the longest part substring
        while length > 0:
            # Flag to check if a part substring is found
            ok = False
            # Iterate through all possible starting indices of substrings of length 'length' in the word
            for i in range(len(s) - length + 1):
                # Check if the substring starting at index 'i' with length 'length' is in the parts set
                if s[i:][:length] in parts:
                    # If found, modify the word by enclosing the part substring within square brackets
                    s = s[:i] + '[%s]' % s[i:][:length] + s[i + length:]
                    # Set flag to True indicating that a part substring is found
                    ok = True
                    # Exit the inner loop as we found the longest part substring
                    break
            
            # If a part substring is found, exit the outer loop
            if ok:
                break
            
            # Decrement the length to check for shorter part substrings
            length -= 1
        
        # Add the modified word to the result list
        ans += [s]
    
    # Return the list of modified words
    return ans