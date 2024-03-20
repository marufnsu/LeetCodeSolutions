"""
Note: Write a solution with O(operations.length) complexity, 
since this is what you would be asked to do during a real interview.

Implement a modified stack that, in addition to using push and pop operations, 
allows you to find the current minimum element in the stack by using a min operation.

Example
For operations = ["push 10", "min", "push 5", "min", "push 8", "min", "pop", "min", "pop", "min"], the output should be
solution(operations) = [10, 5, 5, 5, 10].

The operations array contains 5 instances of the min operation. The results array contains 5 numbers, 
each representing the minimum element in the stack at the moment when min was called.
"""

def solution(operations):
    stack = []  # Initialize an empty stack
    result = []  # Initialize an empty list to store results
    for operation in operations:
        if operation == 'min':  # If the operation is 'min'
            result.append(stack[-1])  # Append the top element of the stack to the result list
        elif operation == "pop":  # If the operation is 'pop'
            stack.pop()  # Remove the top element from the stack
        else:  # If the operation is not 'min' or 'pop'
            num = int(operation.split()[1])  # Extract the number from the operation string
            if stack:  # If the stack is not empty
                # Append the minimum of the current top element and the extracted number to the stack
                stack.append(min(stack[-1], num))
            else:  # If the stack is empty
                stack.append(num)  # Append the extracted number to the stack
    return result  # Return the list of results