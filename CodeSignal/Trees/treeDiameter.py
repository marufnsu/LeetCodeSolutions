"""
You got sick because of walking in the woods at night, and have to spend a week at home without going out. 
Looking out of the window at the nearby woods you're wondering if there is anything you don't yet know about them. 
Suddenly you see a beautiful and very tall tree you haven't seen before. 
Since you have nothing to do, you decide to examine its structure and draw it in your notebook.

You became so exited about this new tree that your temperature went up, so you were forced to stay in bed. 
You can't see the tree from your bed, but luckily you have it drawn down. 
The first thing you'd like to find out about is the tree height. 
Looking at your drawing you suddenly realize that you forgot to mark the tree bottom 
and you don't know from which vertex you should start counting. 
Of course a tree height can be calculated as the length of the longest path in it (it is also called tree diameter).
So, now you have a task you need to solve, so go ahead!

Example

For n = 10 and

tree = [[2, 5], [5, 7], [5, 1], [1, 9], [1, 0], [7, 6], [6, 3], [3, 8], [8, 4]]
the output should be solution(n, tree) = 7.
"""

from collections import defaultdict

def solution(n, tree):
    # Create an adjacency list representation of the tree
    adjacency_list = defaultdict(list)
    for u, v in tree:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    
    # Perform depth-first search (DFS) to find the farthest vertex and its distance
    def dfs(node, parent, distance):
        nonlocal farthest_node, max_distance
        if distance > max_distance:
            farthest_node, max_distance = node, distance
        for neighbor in adjacency_list[node]:
            if neighbor != parent:
                dfs(neighbor, node, distance + 1)
    
    farthest_node, max_distance = 0, 0
    dfs(0, -1, 0)  # Start DFS from any vertex, e.g., vertex 0
    
    # Perform DFS from the farthest node to find the maximum distance again
    max_distance = 0
    dfs(farthest_node, -1, 0)
    
    return max_distance