"""
Reverse bits of a given 32 bits unsigned integer.
"""


class Solution:
    # Note to self: learn what the fuck bitshift is and how to use it
    def reverse_bits(self, n: int) -> int:
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret
