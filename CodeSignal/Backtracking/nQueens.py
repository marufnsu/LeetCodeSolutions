"""
DIFFICULTY LEVEL: HARD
In chess, queens can move any number of squares vertically, horizontally, or diagonally. 
The n-queens puzzle is the problem of placing n queens on an n × n chessboard so that no two queens can attack each other.

Given an integer n, print all possible distinct solutions to the n-queens puzzle. 
Each solution contains distinct board configurations of the placement of the n queens, 
where the solutions are arrays that contain permutations of [1, 2, 3, .. n]. 
The number in the ith position of the results array indicates that the ith column queen is placed in the row with that number. 
In your solution, the board configurations should be returned in lexicographical order.

Example

For n = 1, the output should be
solution(n) = [[1]];

For n = 4, the output should be

  solution(n) = [[2, 4, 1, 3],
                 [3, 1, 4, 2]]
This diagram of the second permutation, [3, 1, 4, 2], will help you visualize its configuration:

The element in the 1st position of the array, 3, indicates that the queen for column 1 is placed in row 3. 
Since the element in the 2nd position of the array is 1, the queen for column 2 is placed in row 1. 
The element in the 3rd position of the array is 4, meaning that the queen for column 3 is placed in row 4, 
and the element in the 4th position of the array is 2, meaning that the queen for column 4 is placed in row 2.
"""

def solution(n):
    ans = []  # List to store all valid column configurations
    
    # Helper function to recursively search for valid column configurations
    def search(cols = []):
        # If the length of the column list equals N, we've found a valid configuration
        if len(cols) == n:
            ans.append(cols)  # Add the current configuration to the result
            return
        
        # Iterate through each column (1 to N)
        for y in range(1, n+1):
            # Check if the current column is not already in the configuration
            if y not in cols:
                # Check if placing a queen at the current column would not conflict with existing queens
                if not any(y + len(cols) == x + i or y - len(cols) == x - i
                           for i, x in enumerate(cols)):
                    # If no conflicts, recursively search for the next column
                    search(cols + [y])
    
    # Start the search from an empty configuration
    search()
    return ans

"""
Explanation:

The solution function takes a sorted array arr and an integer num.
It initializes an empty list result to store the unique subsets.
Inside the function, there is a helper function find_subsets used to recursively find all subsets with the given sum.
The find_subsets function takes three parameters: index (current index in arr), current_sum (current sum of elements in the subset), and subset (current subset being constructed).
If current_sum equals num, it means we've found a subset with the desired sum, so it is added to the result.
Otherwise, it iterates through the remaining elements in arr, adding them to the subset if adding the current element doesn't exceed the target sum.
Recursively, it continues to search for subsets with the updated sum and subset.
After each recursive call, the last element is removed from the subset (backtracking) to explore other possibilities.
The search is initiated by calling find_subsets with an initial index of 0, sum of 0, and an empty subset.
Finally, the list of unique subsets is returned.
"""