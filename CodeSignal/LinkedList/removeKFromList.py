"""
Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in the list, since this is what you'll be asked to do during an interview.
Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.

Example
For l = [3, 1, 2, 3, 4, 5] and k = 3, the output should be
solution(l, k) = [1, 2, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7] and k = 10, the output should be
solution(l, k) = [1, 2, 3, 4, 5, 6, 7].
"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l, k):
    # Handle the case where the first node(s) have value k
    # Skip all nodes at the beginning that have value k
    while l is not None and l.value == k:
        l = l.next
    
    # If the entire list has value k, return None
    if l is None:
        return None
    
    # Start from the first node after skipping nodes with value k
    current = l
    # Iterate through the list
    while current.next is not None:
        # If the next node has value k, skip it by modifying the next pointer
        if current.next.value == k:
            current.next = current.next.next
        # Move to the next node
        else:
            current = current.next
    # Return the updated list
    return l

"""
def solution(l, k):
    c = l
    while c:
        if c.next and c.next.value == k:
            c.next = c.next.next
        else:
            c = c.next
    return l.next if l and l.value == k else l
"""