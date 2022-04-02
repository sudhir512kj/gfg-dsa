"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.
"""

from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        profit = [[0 for i in range(n + 1)]
                 for j in range(k+1)]
        
        for i in range(1, k+1):
            prevDiff = float('-inf')

            for j in range(1, n):
                prevDiff = max(prevDiff,
                               profit[i - 1][j - 1] -
                               prices[j - 1])
                profit[i][j] = max(profit[i][j - 1],
                                   prices[j] + prevDiff)

        return profit[k][n - 1]