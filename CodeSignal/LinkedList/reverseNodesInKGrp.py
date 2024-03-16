"""
Given a linked list l, reverse its nodes k at a time and return the modified list. 
k is a positive integer that is less than or equal to the length of l. 
If the number of nodes in the linked list is not a multiple of k, 
then the nodes that are left out at the end should remain as-is.

You may not alter the values in the nodes - only the nodes themselves can be changed.

Example
For l = [1, 2, 3, 4, 5] and k = 2, the output should be
solution(l, k) = [2, 1, 4, 3, 5];
For l = [1, 2, 3, 4, 5] and k = 1, the output should be
solution(l, k) = [1, 2, 3, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] and k = 3, the output should be
solution(l, k) = [3, 2, 1, 6, 5, 4, 9, 8, 7, 10, 11].
"""


def solution(l, k):
    # Initialize 'current' to the head of the list
    current = l
    
    # Traverse 'k' steps forward
    for _ in range(k):
        # If 'current' becomes None before reaching 'k' nodes,
        # return the original list as it is
        if not current:
            return l
        # Move 'current' to the next node
        current = current.next
    
    # Initialize 'result' to the original head of the list
    result = l
    # Move 'current' to the second node of the reversed group
    current = l.next
    
    # Reverse the first 'k' nodes
    for _ in range(k - 1):
        # Store the next node of 'current' temporarily
        nxt = current.next
        # Reverse the pointer of 'current' to point to 'result'
        current.next = result
        # Move 'current' and 'result' one step forward
        result, current = current, nxt
    
    # Reverse the pointer of the original head node
    # to point to the next reversed group (recursive call)
    l.next = solution(current, k)
    
    # Return the new head of the reversed list
    return result