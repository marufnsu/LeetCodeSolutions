"""
Note: Your solution should have only one BST traversal and O(1) extra space complexity, since this is what you will be asked to accomplish in an interview.

A tree is considered a binary search tree (BST) if for each of its nodes the following is true:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and the right subtrees must also be binary search trees.
Given a binary search tree t, find the kth smallest element in it.

Note that kth smallest element means kth element in increasing order. See examples for better understanding.

Example

For

t = {
    "value": 3,
    "left": {
        "value": 1,
        "left": null,
        "right": null
    },
    "right": {
        "value": 5,
        "left": {
            "value": 4,
            "left": null,
            "right": null
        },
        "right": {
            "value": 6,
            "left": null,
            "right": null
        }
    }
}
and k = 4, the output should be
solution(t, k) = 5.

Here is what t looks like:

   3
 /   \
1     5
     / \
    4   6
The values of t are [1, 3, 4, 5, 6], and the 4th smallest is 5.
"""

#
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

def solution(t, k):
    stack = []  # Initialize an empty stack to perform iterative inorder traversal
    
    while stack or t:  # Continue traversal until the stack is empty and there are no more nodes to visit
        while t:  # Traverse to the leftmost node and push all encountered nodes onto the stack
            stack.append(t)
            t = t.left
            
        t = stack.pop()  # Pop the top node from the stack (current node)
        k -= 1  # Decrement k to keep track of the number of nodes visited
        
        if k == 0:  # If k becomes 0, it means we have reached the kth node in inorder traversal
            return t.value  # Return the value of the kth node
            
        t = t.right  # Move to the right child of the current node to explore its subtree
        
    return None  # Return None if k exceeds the number of nodes in the tree or the tree is empty