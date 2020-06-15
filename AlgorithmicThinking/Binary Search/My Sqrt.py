"""
~Implement int sqrt(int x).

~Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

~Since the return type is an integer,
    the decimal digits are truncated and only the integer part of the result is returned.
"""


class Solution:
    def my_sqrt(self, x: int) -> int:
        if x < 2:
            return x

        l, r = 0, x

        while l <= r:
            half = (l + r) // 2
            half_sqrd = half ** 2
            if half_sqrd == x:
                return half
            elif half_sqrd > x:
                r = half - 1
            else:
                l = half + 1

        return r