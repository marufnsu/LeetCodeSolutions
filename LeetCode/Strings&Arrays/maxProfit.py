'''
121. Best Time to Buy and Sell Stock
Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        max_prof = 0

        for price in prices[1:]:
            if price < min_p:
                min_p = price
            if price - min_p > max_prof:
                max_prof = price - min_p
        return max_prof

"""
def max_profit(prices):
    left, right = 0, 1
    maxP = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxP = max(maxP, profit)
        else:
            left = right
        right += 1
"""