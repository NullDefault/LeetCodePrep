"""
Write a function that takes an unsigned integer and return the number of '1' bits it has
    (also known as the Hamming weight).
"""


class Solution:
    def hamming_weight(self, n: int) -> int:
        weight = 0
        while n != 0:
            weight += 1
            n = n & (n-1)
        return weight
