"""
A tree is considered a binary search tree (BST) if for each of its nodes the following is true:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and the right subtrees must also be binary search trees.
Removing a value x from a BST t is done in the following way:

If there is no x in t, nothing happens;
Otherwise, let t' be a subtree of t such that t'.value = x.
If t' has a left subtree, remove the rightmost node from it and put it at the root of t';
Otherwise, remove the root of t' and its right subtree becomes the new t's root.
For example, removing 4 from the following tree has no effect because there is no such value in the tree:

    5
   / \
  2   6
 / \   \
1   3   8
       /
      7
Removing 5 causes 3 (the rightmost node in left subtree) to move to the root:

    3
   / \
  2   6
 /     \
1       8
       /
      7
And removing 6 after that creates the following tree:

    3
   / \
  2   8
 /   /
1   7
You're given a binary search tree t and an array of numbers queries. Your task is to remove queries[0], queries[1], etc., 
from t, step by step, following the algorithm above. Return the resulting BST.
"""

# Definition for binary tree:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

def solution(t, queries):
    # Function to find the maximum value in a tree rooted at 't'
    def max_of_tree(t):
        if t is None:
            return None
        # Traverse to the rightmost node to find the maximum value
        while t.right is not None:
            t = t.right
        return t.value

    # Function to remove the rightmost node in a tree rooted at 't'
    def remove_right(t):
        # If the right child is None, return the left child
        if t.right is None:
            return t.left
        # Recursively remove the rightmost node
        else:
            t.right = remove_right(t.right)
        return t

    # Function to remove a node with value 'q' from a BST rooted at 't'
    def f1(t, q):
        # If tree is empty, return None
        if t is None:
            return None
        # If the value to remove is found at the current node
        if q == t.value:
            # If the current node has a left child, replace its value with the maximum value in the left subtree
            # and remove the rightmost node in the left subtree
            if t.left:
                t.value = max_of_tree(t.left)
                t.left = remove_right(t.left)
            # If the current node has no left child, replace it with its right child
            else:
                t = t.right
        # If the value to remove is less than the current node's value, go to the left subtree
        elif q < t.value:
            t.left = f1(t.left, q)
        # If the value to remove is greater than the current node's value, go to the right subtree
        elif q > t.value:
            t.right = f1(t.right, q)
        return t

    # Iterate through each query and apply the removal process
    for q in queries:
        t = f1(t, q)

    return t
