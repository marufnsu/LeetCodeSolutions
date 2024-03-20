"""
We're going to store numbers in a tree. Each node in this tree will store a single digit (from 0 to 9), and each path from root to leaf encodes a non-negative integer.

Given a binary tree t, find the sum of all the numbers encoded in it.

Example
For
t = {
    "value": 1,
    "left": {
        "value": 0,
        "left": {
            "value": 3,
            "left": null,
            "right": null
        },
        "right": {
            "value": 1,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 4,
        "left": null,
        "right": null
    }
}
the output should be
solution(t) = 218.
There are 3 numbers encoded in this tree:

Path 1->0->3 encodes 103
Path 1->0->1 encodes 101
Path 1->4 encodes 14
and their sum is 103 + 101 + 14 = 218.
"""

# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

def solution(t, total = 0):
    # Base case: If the current node is None, return 0
    if not t:
        return 0
    
    # If the current node is a leaf node (both left and right children are None),
    # return the accumulated sum multiplied by 10 and add the value of the leaf node
    if t and not t.left and not t.right:
        return 10 * total + t.value
    
    # Recursively compute the sum for the left and right subtrees
    left_sum = solution(t.left, 10 * total + t.value)
    right_sum = solution(t.right, 10 * total + t.value)
    
    # Return the sum of the left and right subtrees
    return left_sum + right_sum


"""
Explanation of the code:

* The function solution takes a binary tree t and an optional parameter s, 
which represents the accumulated sum of the path from the root to the current node. By default, s is initialized to 0.
* In the base case, if the current node t is None (indicating an empty subtree), the function returns 0.
* If the current node t is a leaf node (i.e., both left and right children are None), 
the function returns the accumulated sum s multiplied by 10, to shift digits one place to the left, 
and adds the value of the leaf node. This represents the complete number encoded by the path from the root to the leaf node.
* If the current node t is not a leaf node, the function recursively computes the sum for the left and right subtrees. 
The accumulated sum s is updated by multiplying it by 10 and adding the value of the current node t.value. 
This updated accumulated sum is passed to the recursive calls for the left and right subtrees.
* Finally, the function returns the sum of the results obtained from the left and right subtrees, 
representing the total sum of all the numbers encoded in the binary tree.
"""

