"""
You have an array of integers nums and an array queries, where queries[i] is a pair of indices (0-based). 
Find the sum of the elements in nums from the indices at queries[i][0] to queries[i][1] (inclusive) for each query, 
then add all of the sums for all the queries together. Return that number modulo 109 + 7.

Example
For nums = [3, 0, -2, 6, -3, 2] and queries = [[0, 2], [2, 5], [0, 5]], the output should be
solution(nums, queries) = 10.

The array of results for queries is [1, 3, 6], so the answer is 1 + 3 + 6 = 10.
"""

def solution(nums, queries):
    # Initialize an array to store the cumulative sum at each index
    sum_at = [0] * len(nums)
    
    total = 0  # Initialize total sum
    for i, x in enumerate(nums):
        total += nums[i]  # Add the current number to the total sum
        sum_at[i] = total  # Store the cumulative sum at the current index
    
    ans = [0] * len(queries)  # Initialize ans with the length of queries
    for i, q in enumerate(queries):
        start, end = q
        if start == 0: 
            ans[i] = sum_at[end]  # If start is 0, sum from index 0 to end directly
        else:
            ans[i] = sum_at[end] - sum_at[start - 1]  # Otherwise, subtract cumulative sum at start-1 from cumulative sum at end
        
    return sum(ans) % (10**9 + 7)  # Return the sum of all sums taken modulo 10^9 + 7

"""
Explanation:

sum_at: This list stores the cumulative sum of elements in the nums array. Each element sum_at[i] represents the sum of elements from index 0 to i in the nums array.
total: This variable tracks the running total sum of elements.
The first loop calculates the cumulative sum of elements and populates the sum_at array.
The second loop iterates through each query. For each query [start, end], it calculates the sum of elements from index start to end using the cumulative sum array sum_at.
If start is 0, the sum can be directly obtained from sum_at[end]. Otherwise, the sum is calculated as sum_at[end] - sum_at[start - 1].
The total sum of all elements in the ans array is calculated, and modulo operation is performed with (10**9 + 7) as required by the problem statement. Finally, the result is returned.
"""