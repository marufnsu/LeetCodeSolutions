"""
Note: Try to solve this task in O(n2) time, where n is a number of vertices, since this is what you'll be asked to do during an interview.

Sue is a network administrator who consults for companies that have massive Local Area Networks (LANs). 
The computers are connected together with network cables, and Sue has been brought in to evaluate the company’s network. 
The networks are huge, and she wants to ensure that no single network cable failure can disconnect the network. 
Any cable that fails that leaves the network in two or more disconnected pieces is called a single point of failure.

She labels the different network devices from 0 to n - 1. She keeps an n × n matrix connections, 
where connections[i][j] = 1 if there is a network cable directly connecting devices i and j, and 0 otherwise. 
Write a function that takes the matrix of connections, and returns the number of cables that are a single point of failure.

Example
For connections = [[0, 1], [1, 0]], the output should be
solution(connections) = 1.
A failure of the cable that connects devices 0 and 1 would leave the network disconnected.

For connections = [[0, 1, 1], [1, 0, 1], [1, 1, 0]], the output should be
solution(connections) = 0.
No failure of a single network cable would result in the network being disconnected.

For connections = [[0, 1, 1, 1, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0]], the output should be
solution(connections) = 3.
The three cables that are single points of failure are connected with device 3:

For connections = [[0, 1, 1, 1, 1], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]], the output should be
solution(connections) = 4.
"""

def solution(connections):
    COUNT = 0  # Counter to keep track of the number of cycles
    recursed = [False] * len(connections)  # List to track if a node has been visited in the current recursion
    visited = [False] * len(connections)  # List to track if a node has been visited in any recursion
    
    non_cycle_edges = {}  # Dictionary to store non-cycle edges (not used in the provided code)
    
    def dfs(root, parent):
        nonlocal COUNT
        nonlocal recursed
        nonlocal visited 
        
        # If the node has been visited in the current path, a cycle is detected
        if visited[root]:
            return [root]  # Return the start node of the cycle
        
        # If the node has been recursed before, don't process it again to avoid duplication of work
        elif recursed[root]:
            return None
        
        recursed[root] = True  # Mark the node as visited in the current recursion
        visited[root] = True  # Mark the node as visited in any recursion

        ret = []  # List to store the start nodes of cycles
        
        # Traverse through the neighbors of the current node
        for i in range(len(connections)):
            if connections[root][i] and i != parent:
                # Recursively explore the neighbor nodes
                starts_of_cycles = dfs(i, root)
                if starts_of_cycles is None:
                    pass 
                elif len(starts_of_cycles) > 0:
                    # Add start nodes of cycles to the result list
                    ret.extend([x for x in starts_of_cycles if x != root])
                else:
                    print((root, i, parent))  # Debugging statement
                    
                    COUNT += 1  # Increment the cycle count
                    
        # Remove the current node from visited to backtrack
        visited[root] = False
        return ret
    
    dfs(0, None)  # Start DFS from the root node (0)
    return COUNT  # Return the total count of cycles

"""
* The function solution takes a list of connections representing a graph and counts the number of cycles in the graph.
* It uses a depth-first search (DFS) approach to traverse the graph and detect cycles.
* The dfs function recursively explores the graph starting from a given node (root). 
It marks nodes as visited (recursed and visited lists) and detects cycles during the traversal.
* The cycles are counted, and the total count is returned as the result.




"""