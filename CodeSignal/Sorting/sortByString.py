"""
Sort the letters in the string s by the order they occur in the string t.

Example

For s = "weather" and t = "therapyw", the output should be
solution(s, t) = "theeraw";

For s = "good" and t = "odg", the output should be
solution(s, t) = "oodg".
"""

def solution(s, t):
    # Create a dictionary to store the indices of characters in string t
    char_indices = {char: idx for idx, char in enumerate(t)}
    
    # Define a custom sorting function based on the indices in string t
    def custom_sort(char):
        return char_indices.get(char, float('inf'))
    
    # Sort the characters in string s using the custom sorting function
    sorted_s = sorted(s, key=custom_sort)
    
    # Return the sorted string
    return ''.join(sorted_s)


"""
def solution(s, t):
    return "".join(sorted(s, key=lambda char: t.find(char)))
"""