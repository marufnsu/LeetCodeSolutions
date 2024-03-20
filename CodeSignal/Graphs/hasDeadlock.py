"""
In a multithreaded environment, it's possible that different processes will need to use the same resource. 
A wait-for graph represents the different processes as nodes in a directed graph, 
where an edge from node i to node j means that the node j is using a resource that 
node i needs to use (and cannot use until node j releases it).

We are interested in whether or not this digraph has any cycles in it. 
If it does, it is possible for the system to get into a state where no process can complete.

We will represent the processes by integers 0, ...., n - 1. We represent the edges using a two-dimensional list connections. 
If j is in the list connections[i], then there is a directed edge from process i to process j.

Write a function that returns True if connections describes a graph with a directed cycle, or False otherwise.

Example
For connections = [[1], [2], [3, 4], [4], [0]], the output should be
solution(connections) = true.
This graph contains a cycle.

For connections = [[1, 2, 3], [2, 3], [3], []], the output should be
solution(connections) = false.
This graph doesn't contain a directed cycle (there are two paths from 0 to 3, but no paths from 3 back to 0).
"""

def solution(connections):
    def has_cycle(node, visited, recursion_stack):
        visited[node] = True
        recursion_stack[node] = True

        for neighbor in connections[node]:
            if not visited[neighbor]:
                if has_cycle(neighbor, visited, recursion_stack):
                    return True
            elif recursion_stack[neighbor]:
                return True

        recursion_stack[node] = False
        return False

    n = len(connections)
    visited = [False] * n
    recursion_stack = [False] * n

    for node in range(n):
        if not visited[node]:
            if has_cycle(node, visited, recursion_stack):
                return True

    return False

"""
In this solution:

* We define a nested function has_cycle to perform DFS traversal and detect cycles. 
It takes a node, a boolean array visited to mark visited nodes, 
and a boolean array recursion_stack to track nodes in the current recursion stack.
* Within has_cycle, we mark the current node as visited and add it to the recursion stack. 
Then, we traverse its neighbors recursively.
* If a neighbor is visited and also present in the recursion stack, 
it indicates a back edge and hence a cycle.
* Finally, we iterate over all nodes in the graph and call has_cycle for each unvisited node. 
If any node leads to a cycle, we return True; otherwise, we return False indicating no cycle is present.
"""