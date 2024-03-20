"""
DIFFICULTY LEVEL: HARD
Given an array of integers a, return a new array b using the following guidelines:

For each index i in b, the value of bi is the index of the aj nearest to ai and is also greater than ai.
If there are two options for bi, put the leftmost one in bi.
If there are no options for bi, put -1 in bi.
Example

For a = [1, 4, 2, 1, 7, 6], the output should be
solution(a) = [1, 4, 1, 2, -1, 4].

for a[0], the nearest larger element is 4 at index a[1] -> b[0] contains the value 1.
for a[1], the nearest larger element is 7 at a[4] -> b[1] contains the value 4.
for a[2], the nearest larger element is 4 at a[1] (7 is also larger, but 4 has the minimal position) -> b[2] contains the value 1.
for a[3], the nearest larger element is 2 at a[2] (7 is also larger, but 2 has the minimal position) -> b[3] contains the value 2.
for a[4], there is no element larger than 7 -> b[4] contains the value -1.
for a[5], the nearest larger element is 7 at a[4] -> b[5] contains the value 4.
"""

def solution(a):
    # Initialize arrays b and stack
    # b will store the result, stack is used for tracking indices
    b, stack = [-1] * len(a), []
    
    # Iterate through each element of array a
    for i in range(len(a)):
        # Process elements in the stack until it's empty or the current element is greater than the top element in the stack
        while stack and a[stack[-1]] < a[i]:
            # Pop the top element from the stack
            j = stack.pop()
            # Update b[j] if it's still -1 or if the distance between the current index i and j is smaller than the previous distance
            if b[j] == -1 or (i - j) < (j - b[j]): 
                b[j] = i
        
        # If the stack is empty, there's no element to the left that is greater than the current element
        # So, set b[i] to -1
        if not stack: 
            b[i] = -1
        else: 
            # If the top element in the stack has the same value as the current element, copy b[stack[-1]] to b[i]
            # Otherwise, set b[i] to the top element in the stack
            b[i] = stack[-1] if a[i] != a[stack[-1]] else b[stack[-1]]    
        
        # Append the current index to the stack
        stack.append(i)
    
    # Return the result array b
    return b