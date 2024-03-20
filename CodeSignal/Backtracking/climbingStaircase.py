"""
You need to climb a staircase that has n steps, and you decide to get some extra exercise by jumping up the steps. 
You can cover at most k steps in a single jump. Return all the possible sequences of jumps that you could take to climb the staircase, sorted.

Example
For n = 4 and k = 2, the output should be

solution(n, k) =
[[1, 1, 1, 1],
 [1, 1, 2],
 [1, 2, 1],
 [2, 1, 1],
 [2, 2]]
There are 4 steps in the staircase, and you can jump up 2 or fewer steps at a time. 
There are 5 potential sequences in which you jump up the stairs either 2 or 1 at a time.
"""
def solution(n, k):
    # If n is negative, return an empty list (invalid case)
    if n < 0: 
        return []
    # If n is 0, return a list containing an empty sequence (base case)
    if n == 0: 
        return [[]]
    
    ans = []
    # Iterate from 1 to k (maximum steps allowed in a single jump)
    for i in range(1, k+1):
        # Recursively call the function with remaining steps and update the sequence
        for seq in solution(n-i, k):
            # Append the current jump size to the sequence
            ans.append([i] + seq)
    
    # Return the list of all possible sequences of jumps
    return ans


"""
def solution(n, k):
    def generate_sequences(curr_sequence, remaining_steps):
        # Base case: If there are no remaining steps, add the current sequence to the result
        if remaining_steps == 0:
            result.append(curr_sequence)
            return
        
        # Recursive case: Generate sequences by taking jumps of size from 1 to k
        for jump in range(1, min(remaining_steps, k) + 1):
            generate_sequences(curr_sequence + [jump], remaining_steps - jump)
    
    result = []
    generate_sequences([], n)
    return result
"""