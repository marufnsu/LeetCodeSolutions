"""
Given a binary tree t and an integer s, determine whether there is a root to leaf path in t such that the sum of vertex values equals s.

Example

For

t = {
    "value": 4,
    "left": {
        "value": 1,
        "left": {
            "value": -2,
            "left": null,
            "right": {
                "value": 3,
                "left": null,
                "right": null
            }
        },
        "right": null
    },
    "right": {
        "value": 3,
        "left": {
            "value": 1,
            "left": null,
            "right": null
        },
        "right": {
            "value": 2,
            "left": {
                "value": -2,
                "left": null,
                "right": null
            },
            "right": {
                "value": -3,
                "left": null,
                "right": null
            }
        }
    }
}
and
s = 7,
the output should be solution(t, s) = true.

This is what this tree looks like:

      4
     / \
    1   3
   /   / \
  -2  1   2
    \    / \
     3  -2 -3
Path 4 -> 3 -> 2 -> -2 gives us 7, the required sum.

"""
class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def solution(t, s):
    # Base case: If the t is None, return False
    if t is None:
        return False

    # Subtract the current t's value from the target sum
    s -= t.value

    # If we reach a leaf t and the target sum becomes zero, return True
    if t.left is None and t.right is None:
        return s == 0

    # Recursively check for root-to-leaf paths in the left and right subtrees
    return solution(t.left, s) or solution(t.right, s)
