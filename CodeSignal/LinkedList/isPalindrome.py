"""
Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in l, since this is what you'll be asked to do during an interview.
Given a singly linked list of integers, determine whether or not it's a palindrome.
Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: in real data you will be given a head node l of the linked list

Example
For l = [0, 1, 0], the output should be
solution(l) = true;

For l = [1, 2, 2, 3], the output should be
solution(l) = false.
"""

# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def reverse_linked_list(head):
    # Initialize previous node as None
    prev = None
    # Current node starts from the head
    current = head
    # Iterate through the linked list
    while current:
        # Store the next node in a variable
        next_node = current.next
        # Reverse the link to the previous node
        current.next = prev
        # Move previous pointer to the current node
        prev = current
        # Move current pointer to the next node
        current = next_node
    # Return the new head of the reversed linked list
    return prev

def solution(l):
    # Find the middle of the linked list using slow and fast pointers
    slow = l
    fast = l
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse the second half of the linked list
    reversed_second_half = reverse_linked_list(slow)
    
    # Compare the first half with the reversed second half
    while reversed_second_half:
        # If values don't match, linked list is not a palindrome
        if l.value != reversed_second_half.value:
            return False
        # Move to the next nodes in both halves
        l = l.next
        reversed_second_half = reversed_second_half.next
    
    # If all values match, linked list is a palindrome
    return True