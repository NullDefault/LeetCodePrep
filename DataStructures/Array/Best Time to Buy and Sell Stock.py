"""
~Say you have an array prices for which the ith element is the price of a given stock on day i.

~Design an algorithm to find the maximum profit. You may complete as many transactions as you like
    (i.e., buy one and sell one share of the stock multiple times).

~Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        last = 10 ** 4
        profit = 0
        for p in prices:
            if p > last:
                profit += p - last
            last = p
        return profit