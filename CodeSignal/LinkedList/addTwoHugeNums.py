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
    a = reverse(a)
    b = reverse(b)
    
    carry = 0
    result = None
    
    while a is not None or b is not None or carry > 0:
        raw = ((a.value if a is not None else 0) + 
               (b.value if b is not None else 0) + 
               carry)
                
        node = ListNode(raw % 10000)
        node.next = result
        
        result = node
        carry = raw // 10000
        
        if a is not None:
            a = a.next
        if b is not None:
            b = b.next
            
    return result
    
def reverse(list):
    current = list
    previous = None
    
    while current is not None:
        previous, current.next, current = current, previous, current.next
        
    return previous