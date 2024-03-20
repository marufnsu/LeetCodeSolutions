"""
Given an encoded string, return its corresponding decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times. Note: k is guaranteed to be a positive integer.

Note that your solution should have linear complexity because this is what you will be asked during an interview.

Example

For s = "4[ab]", the output should be
solution(s) = "abababab";

For s = "2[b3[a]]", the output should be
solution(s) = "baaabaaa";

For s = "z1[y]zzz2[abc]", the output should be
solution(s) = "zyzzzabcabc".
"""

def solution(s):
    stack = []  # Initialize a stack to store characters and counts
    current_count = 0  # Initialize current_count to store the count of characters

    for char in s:
        if char.isdigit():  # If the character is a digit, update current_count
            current_count = current_count * 10 + int(char)
        elif char == '[':  # If the character is '[', push current_count and reset it
            stack.append(current_count)
            current_count = 0
        elif char == ']':  # If the character is ']', decode the substring
            substr = ''  # Initialize a substring to store the decoded characters
            while stack and isinstance(stack[-1], str):  # Pop characters until a count is encountered
                substr = stack.pop() + substr
            count = stack.pop()  # Pop the count of the substring
            stack.append(count * substr)  # Multiply the substring by the count and push it back
        else:  # If the character is a letter, push it to the stack
            stack.append(char)

    return ''.join(stack)  # Join the characters in the stack to form the decoded string