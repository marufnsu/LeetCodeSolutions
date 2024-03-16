"""
Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an interview.
Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, 
that contains the elements from both original lists.

Example

For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
solution(l1, l2) = [1, 2, 3, 4, 5, 6];
For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
solution(l1, l2) = [0, 1, 1, 2, 3, 4, 5].
"""

# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def solution(l1, l2):
    # Create a dummy node to serve as the head of the result linked list
    dummy_head = ListNode(0)
    current = dummy_head
    
    # Iterate over both linked lists simultaneously
    while l1 and l2:
        # Compare the values of the current nodes of both lists
        if l1.value <= l2.value:
            # If the value of l1 is smaller or equal, append l1 node to the result list
            current.next = l1
            # Move to the next node in l1
            l1 = l1.next
        else:
            # If the value of l2 is smaller, append l2 node to the result list
            current.next = l2
            # Move to the next node in l2
            l2 = l2.next
        # Move the current pointer to the next node in the result list
        current = current.next
    
    # Append any remaining nodes from l1 or l2
    if l1:
        current.next = l1
    if l2:
        current.next = l2
    
    # Return the result linked list, skipping the dummy head
    return dummy_head.next
