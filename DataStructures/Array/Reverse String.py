"""
~Write a function that reverses a string. The input string is given as an array of characters char[].

~Do not allocate extra space for another array,
    you must do this by modifying the input array in-place with O(1) extra memory.

~You may assume all the characters consist of printable ascii characters.
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s = s.reverse()
        # This also works
        # s = s[::-1]
