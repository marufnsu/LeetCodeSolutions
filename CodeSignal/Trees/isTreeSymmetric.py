"""
Given a binary tree t, determine whether it is symmetric around its center, i.e. each side mirrors the other.

Example

For

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": {
            "value": 3,
            "left": null,
            "right": null
        },
        "right": {
            "value": 4,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 2,
        "left": {
            "value": 4,
            "left": null,
            "right": null
        },
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    }
}
the output should be solution(t) = true.

Here's what the tree in this example looks like:

    1
   / \
  2   2
 / \ / \
3  4 4  3
As you can see, it is symmetric.
"""

class Tree:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def is_mirror(left, right):
    # Base case: If both nodes are None, they are symmetric
    if left is None and right is None:
        return True
    # If one node is None and the other isn't, they are not symmetric
    if left is None or right is None:
        return False
    # Check if the values of corresponding nodes are equal
    # and if the left subtree of left node is mirror of right subtree of right node
    # and if the right subtree of left node is mirror of left subtree of right node
    return (left.value == right.value) and \
           is_mirror(left.left, right.right) and \
           is_mirror(left.right, right.left)

def solution(t):
    # If the tree is empty, it is symmetric
    if t is None:
        return True
    # Check if the left and right subtrees are mirrors of each other
    return is_mirror(t.left, t.right)