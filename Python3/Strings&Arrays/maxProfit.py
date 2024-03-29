'''
Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minP = prices[0]
        maxProfit = 0

        for p in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[p] - minP)
            minP = min(minP, prices[p])

        return maxProfit

"""
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(profit, max_profit)
    return max_profit
"""