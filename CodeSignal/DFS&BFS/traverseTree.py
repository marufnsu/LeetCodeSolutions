"""
Note: Try to solve this task without using recursion, since this is what you'll be asked to do during an interview.

Given a binary tree of integers t, return its node values in the following format:

The first element should be the value of the tree root;
The next elements should be the values of the nodes at height 1 (i.e. the root children), ordered from the leftmost to the rightmost one;
The elements after that should be the values of the nodes at height 2 (i.e. the children of the nodes at height 1) ordered in the same way;
Etc.
"""

def solution(t):
    if t is None:  # If the tree is empty, return an empty list
        return []
    
    results = []  # Initialize a list to store the node values
    t_list = [t]  # Initialize a list with the root node
    
    while t_list:  # Continue iterating as long as the list is not empty
        val = t_list.pop(0)  # Dequeue the first node from the list
        results += [val.value]  # Append the value of the dequeued node to the results list
        
        # Enqueue the left and right children of the dequeued node if they exist
        if val.left:
            t_list += [val.left]
        if val.right:
            t_list += [val.right]
    
    return results  # Return the list containing node values