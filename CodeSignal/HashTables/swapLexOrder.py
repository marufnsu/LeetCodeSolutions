"""
DIFFICULTY LEVEL: HARD
Given a string str and array of pairs that indicates which indices in the string can be swapped, 
return the lexicographically largest string that results from doing the allowed swaps. You can swap indices any number of times.

Example
For str = "abdc" and pairs = [[1, 4], [3, 4]], the output should be
solution(str, pairs) = "dbca".

By swapping the given indices, you get the strings: "cbda", "cbad", "dbac", "dbca". The lexicographically largest string in this list is "dbca".
"""

def solution(str_, pairs):
    n = len(str_)
    str_ = list(str_)  # Convert string to list for easy manipulation

    # Initialize a list to store the indices that are connected
    corr = [set() for _ in range(n)]

    # Initialize a set to store all unique indices
    nodes = set()

    # Populate the 'corr' list and 'nodes' set based on the given pairs
    for a, b in pairs:
        corr[a-1].add(b-1)
        corr[b-1].add(a-1)
        nodes.add(a-1)
        nodes.add(b-1)

    # Iterate until all nodes are processed
    while nodes:
        active = {nodes.pop()}  # Start with an active node
        group = set()  # Initialize a set to store the current group of connected nodes

        # Continue iterating until no more active nodes are available
        while active:
            group |= active  # Add active nodes to the current group
            nodes -= active  # Remove processed nodes from the 'nodes' set
            active = {y for x in active for y in corr[x] if y in nodes}  # Find new active nodes connected to the current ones

        # Sort characters within the current group in descending order
        chars = iter(sorted((str_[i] for i in group), reverse=True))

        # Replace characters in the original string with sorted characters from the group
        for i in sorted(group):
            str_[i] = next(chars)

    # Convert the modified list back to a string and return
    return "".join(str_)
