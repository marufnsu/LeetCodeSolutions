"""
DIFFICULTY LEVEL: HARD
You have a collection of coins, and you know the values of the coins and the quantity of each type of coin in it. 
You want to know how many distinct sums you can make from non-empty groupings of these coins.

Example

For coins = [10, 50, 100] and quantity = [1, 2, 1], the output should be
solution(coins, quantity) = 9.

Here are all the possible sums:

50 = 50;
10 + 50 = 60;
50 + 100 = 150;
10 + 50 + 100 = 160;
50 + 50 = 100;
10 + 50 + 50 = 110;
50 + 50 + 100 = 200;
10 + 50 + 50 + 100 = 210;
10 = 10;
100 = 100;
10 + 100 = 110.
As you can see, there are 9 distinct sums that can be created from non-empty groupings of your coins.
"""

def solution(coins, quantity):
    # Initialize a set to store the possible sums, starting with 0
    possible_sums = {0}
    
    # Iterate through each coin and its quantity
    for coin, quant in zip(coins, quantity):
        # Update the set of possible sums by adding new sums for the current coin
        # Each new sum is generated by adding the coin value multiplied by its quantity
        # to each existing sum in the set, for all possible quantities of the coin
        possible_sums = {total + coin * i for total in possible_sums for i in range(quant + 1)}
    
    # Return the count of possible sums, excluding the 0 sum
    return len(possible_sums) - 1