"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0
        while r < len(prices):
            temp = prices[r] - prices[l]
            if prices[l] < prices[r]:
                profit = max(profit, temp)
            else:
                l = r
            r += 1
        return profit
