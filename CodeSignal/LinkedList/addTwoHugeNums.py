"""
You're given 2 huge integers represented by linked lists. Each linked list element is a number from 0 to 9999 that represents a number with exactly 4 digits. 
The represented number might have leading zeros. Your task is to add up these huge integers and return the result in the same format.

Example
For a = [9876, 5432, 1999] and b = [1, 8001], the output should be
solution(a, b) = [9876, 5434, 0].
Explanation: 987654321999 + 18001 = 987654340000.

For a = [123, 4, 5] and b = [100, 100, 100], the output should be
solution(a, b) = [223, 104, 105].
Explanation: 12300040005 + 10001000100 = 22301040105.
"""

# Definition for singly-linked list:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def solution(a, b):
    # Reverse both input linked lists
    a = reverse(a)
    b = reverse(b)
    
    carry = 0  # Initialize carry to 0
    result = None  # Initialize the result linked list to None
    
    # Iterate until both input linked lists are exhausted and there's no carry left
    while a is not None or b is not None or carry > 0:
        # Calculate the sum of current digits along with the carry
        raw = ((a.value if a is not None else 0) + 
               (b.value if b is not None else 0) + 
               carry)
        
        # Create a new node for the sum digit and update the carry
        node = ListNode(raw % 10000)  # Take the last 4 digits of the sum
        node.next = result  # Append the new node to the result linked list
        
        result = node  # Update the result linked list
        carry = raw // 10000  # Update the carry to the first 4 digits of the sum
        
        # Move to the next node in both input linked lists if they are not None
        if a is not None:
            a = a.next
        if b is not None:
            b = b.next
            
    return result  # Return the resulting linked list
    
def reverse(list):
    current = list  # Initialize current node to the head of the linked list
    previous = None  # Initialize previous node to None
    
    # Reverse the linked list by updating pointers
    while current is not None:
        # Save the next node before changing the current node's pointer
        previous, current.next, current = current, previous, current.next
        
    return previous  # Return the new head of the reversed linked list