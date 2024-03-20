"""
The sum of a subtree is the sum of all the node values in that subtree, including its root.

Given a binary tree of integers, find the most frequent sum (or sums) of its subtrees.

Example
The sum of a subtree is the sum of all the node values in that subtree, including its root.

Given a binary tree of integers, find the most frequent sum (or sums) of its subtrees.

Example

For
t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": null,
        "right": null
    },
    "right": {
        "value": 3,
        "left": null,
        "right": null
    }
}
the output should be
solution(t) = [2, 3, 6].
1st example

Since all the sum values in this tree occur only once, return all of them in ascending order.

For
t = {
    "value": -2,
    "left": {
        "value": -3,
        "left": null,
        "right": null
    },
    "right": {
        "value": 2,
        "left": null,
        "right": null
    }
}
the output should be
solution(t) = [-3].
2nd example

There are 3 subtree sums for this tree: -2 + (-3) + 2 = -3, -3, and -2. The most frequent sum is -3 since it appears twice.
the output should be
solution(t) = [2, 3, 6].
1st example

Since all the sum values in this tree occur only once, return all of them in ascending order.

For
t = {
    "value": -2,
    "left": {
        "value": -3,
        "left": null,
        "right": null
    },
    "right": {
        "value": 2,
        "left": null,
        "right": null
    }
}
the output should be
solution(t) = [-3].
2nd example

There are 3 subtree sums for this tree: -2 + (-3) + 2 = -3, -3, and -2. The most frequent sum is -3 since it appears twice.
"""

# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

# Dictionary to store the sums and their frequencies
sums = {}

# Main function to find the most frequent sum(s) in the binary tree
def solution(t):
    # Calculate the frequencies of sums in the tree
    get_freqs(t)
    # Find the maximum frequency of sums
    mf = max(sums.values()) if sums else -1
    # Return sorted list of sums with maximum frequency
    return sorted(v for v, f in sums.items() if f == mf) if sums else []

# Helper function to calculate the sum of each subtree and update the frequencies
def get_freqs(t):
    # Base case: If tree is empty, return sum of 0
    if t is None:
        return 0
    # Recursively calculate sum of left subtree
    left_sum = get_freqs(t.left)
    # Recursively calculate sum of right subtree
    right_sum = get_freqs(t.right)
    # Calculate sum of current subtree
    current_sum = left_sum + right_sum + t.value
    # Update frequencies dictionary
    sums[current_sum] = sums[current_sum] + 1 if current_sum in sums else 1
    # Return sum of current subtree
    return current_sum