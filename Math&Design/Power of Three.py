"""
~Given an integer, write a function to determine if it is a power of three.
"""


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Note: 3**19 is the highest 32 bit integer that's a power of 3, hence why we use it below
        return n > 0 and 3**19 % n == 0
