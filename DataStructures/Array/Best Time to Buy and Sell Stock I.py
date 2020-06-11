"""
~Say you have an array for which the ith element is the price of a given stock on day i.

~If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
    design an algorithm to find the maximum profit.

~Note that you cannot sell a stock before you buy one.
"""


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        min_price = 2**31
        max_profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            elif p - min_price > max_profit:
                max_profit = p - min_price
        return max_profit
