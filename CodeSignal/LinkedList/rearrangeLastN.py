"""
DIFFICULTY LEVEL: HARD
Given a singly linked list of integers l and a non-negative integer n, 
move the last n list nodes to the beginning of the linked list.

Example
For l = [1, 2, 3, 4, 5] and n = 3, the output should be
solution(l, n) = [3, 4, 5, 1, 2];
For l = [1, 2, 3, 4, 5, 6, 7] and n = 1, the output should be
solution(l, n) = [7, 1, 2, 3, 4, 5, 6].
"""

def solution(l, n):
    # If n is 0, no need to move nodes, return the original list
    if n == 0:
        return l
    
    # Initialize two pointers, front and back, both starting from the head of the list
    front, back = l, l
    
    # Move the front pointer n steps forward
    for _ in range(n):
        front = front.next
    
    # If front pointer reaches the end of the list, no need to move nodes, return the original list
    if not front:
        return l
    
    # Move both front and back pointers until front reaches the end of the list
    while front.next:
        front = front.next
        back = back.next
    
    # Save the node after which nodes need to be moved to the beginning
    out = back.next
    
    # Break the list by setting the next of the back pointer to None
    back.next = None
    
    # Connect the end of the list to the beginning by setting the next of front pointer to the original head of the list
    front.next = l
    
    # Return the node after which nodes were moved to the beginning
    return out