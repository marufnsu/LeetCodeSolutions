"""
DIFFICULTY LEVEL: HARD
Given a sorted array of integers arr and an integer num, find all possible unique subsets of arr that add up to num. 
Both the array of subsets and the subsets themselves should be sorted in lexicographical order.

Example
For arr = [1, 2, 3, 4, 5] and num = 5, the output should be
solution(arr, num) = [[1, 4], [2, 3], [5]].
"""

def solution(arr, num):
    result = []
    
    # Helper function to find all subsets with the given sum
    def find_subsets(index, current_sum, subset):
        if current_sum == num:
            result.append(subset[:])  # Add the current subset to the result
            return
        
        # Iterate through the remaining elements in the array
        for i in range(index, len(arr)):
            # If adding the current element doesn't exceed the target sum, include it in the subset
            if current_sum + arr[i] <= num:
                subset.append(arr[i])
                # Recursively find subsets with the updated sum and subset
                find_subsets(i + 1, current_sum + arr[i], subset)
                subset.pop()  # Backtrack: Remove the last element from the subset
    
    # Start the search from the beginning of the array with an empty subset and sum of 0
    find_subsets(0, 0, [])
    
    return result

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