"""
Given two binary trees t1 and t2, determine whether the second tree is a subtree of the first tree. 
A subtree for vertex v in a binary tree t is a tree consisting of v and all its descendants in t. 
Determine whether or not there is a vertex v (possibly none) in tree t1 such that a subtree for vertex v (possibly empty) in t1 equals t2.

the output should be solution(t1, t2) = true.

This is what these trees look like:

      t1:             t2:
       5              10
      / \            /  \
    10   7          4    6
   /  \            / \    \
  4    6          1   2   -1
 / \    \
1   2   -1
As you can see, t2 is a subtree of t1 (the vertex in t1 with value 10).
"""

# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

def is_equal(tree1, tree2):
    if not tree1 and not tree2:
        return True
    if not tree1 or not tree2:
        return False
    if tree1.value != tree2.value:
        return False
    return is_equal(tree1.left, tree2.left) and is_equal(tree1.right, tree2.right)

def is_subtree(t1, t2):
    if not t2:
        return True
    if not t1:
        return False
    if is_equal(t1, t2):
        return True
    return is_subtree(t1.left, t2) or is_subtree(t1.right, t2)

def solution(t1, t2):
    return is_subtree(t1, t2)
