"""
You have a binary tree t. Your task is to find the largest value in each row of this tree. In a tree, a row is a set of nodes that have equal depth. 
For example, a row with depth 0 is a tree root, a row with depth 1 is composed of the root's children, etc.

Return an array in which the first element is the largest value in the row with depth 0, 
the second element is the largest value in the row with depth 1, the third element is the largest element in the row with depth 2, etc.
For

t = {
    "value": -1,
    "left": {
        "value": 5,
        "left": null,
        "right": null
    },
    "right": {
        "value": 7,
        "left": null,
        "right": {
            "value": 1,
            "left": null,
            "right": null
        }
    }
}
the output should be solution(t) = [-1, 7, 1].

The tree in the example looks like this:

    -1
   / \
  5   7
       \
        1
In the row with depth 0, there is only one vertex - the root with value -1;
In the row with depth 1, there are two vertices with values 5 and 7, so the largest value here is 7;
In the row with depth 2, there is only one vertex with value 1.
"""

import math

def solution(t):
    # Check if the tree is empty
    if t is None:
        return []

    # Initialize a stack with the root node
    stack = [t]
    # Initialize an empty list to store the maximum values
    result = []

    # Continue iteration until the stack is empty
    while len(stack) > 0:
        # Append the maximum value of the current level to the result list
        result.append(max(tree.value for tree in stack))

        # Create a new list to store the nodes of the next level
        next_row = [tree.left for tree in stack if tree.left] + [tree.right for tree in stack if tree.right]
        
        # Replace the stack with the list of nodes for the next level
        stack = next_row

    # Return the list of maximum values
    return result

"""
Explanation:

* The function solution takes a binary tree t as input and returns a list containing the maximum values at each level of the tree.
* The function first checks if the tree is empty. If so, it returns an empty list since there are no maximum values to compute.
* It initializes a stack with the root node of the tree.
* It enters a loop that continues until the stack is empty. Inside the loop:
* It appends the maximum value of the current level to the result list. 
This is achieved by using a generator expression to calculate the maximum value of tree.
value for each node in the current level (stack).
* It constructs a new list next_row containing the nodes of the next level. 
This is done by iterating over the nodes in the current level (stack) and adding their left and right children (if they exist) to the list.
* It updates the stack with the nodes of the next level, ready for the next iteration.
* Finally, it returns the result list containing the maximum values at each level of the tree.
"""
