"""
DIFFICULTY LEVEL: HARD
Note: Your solution should have O(inorder.length) time complexity, since this is what you will be asked to accomplish in an interview.

Let's define inorder and preorder traversals of a binary tree as follows:

Inorder traversal first visits the left subtree, then the root, then its right subtree;
Preorder traversal first visits the root, then its left subtree, then its right subtree.
For example, if tree looks like this:

    1
   / \
  2   3
 /   / \
4   5   6
then the traversals will be as follows:

Inorder traversal: [4, 2, 1, 5, 3, 6]
Preorder traversal: [1, 2, 4, 3, 5, 6]
Given the inorder and preorder traversals of a binary tree t, but not t itself, restore t and return it.
"""

# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

def solution(inorder, preorder):
    # Base case: if either inorder or preorder traversal is empty, return None
    if not inorder or not preorder:
        return None
    
    # Extract the root value from the preorder traversal and create a tree node with that value
    root_val = preorder.pop(0)
    root = Tree(root_val)
    
    # Find the index of the root value in the inorder traversal
    root_index = inorder.index(root_val)
    
    # Recursively build the left subtree using the left part of the inorder traversal and the corresponding part of the preorder traversal
    root.left = solution(inorder[:root_index], preorder)
    
    # Recursively build the right subtree using the right part of the inorder traversal and the corresponding part of the preorder traversal
    root.right = solution(inorder[root_index + 1:], preorder)
    
    # Return the root of the binary tree
    return root