"""
You are climbing a staircase that has n steps. You can take the steps either 1 or 2 at a time. 
Calculate how many distinct ways you can climb to the top of the staircase.

Example

For n = 1, the output should be
solution(n) = 1;

For n = 2, the output should be
solution(n) = 2.

You can either climb 2 steps at once or climb 1 step two times.
"""

def solution(n):
    # Initialize variables a and b to represent the number of ways to reach steps i-1 and i respectively
    a = b = 1
    
    # Loop until n becomes 0
    while n:
        # Update variables a and b to represent the number of ways to reach steps i-1 and i respectively
        a, b = b, a + b
        
        # Decrement n by 1 in each iteration
        n -= 1
        
    # Return the number of ways to reach step n
    return a

"""
def solution(n):
    # Initialize an array to store the number of distinct ways to climb to each step
    dp = [0] * (n + 1)
    # There's only one way to climb 0 or 1 step
    dp[0] = dp[1] = 1
    
    # Calculate the number of distinct ways to climb to each step
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    # Return the number of distinct ways to climb to the top of the staircase
    return dp[n]
"""