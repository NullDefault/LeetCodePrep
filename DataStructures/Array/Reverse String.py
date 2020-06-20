"""
~Write a function that reverses a string. The input string is given as an array of characters char[].

~Do not allocate extra space for another array,
    you must do this by modifying the input array in-place with O(1) extra memory.

~You may assume all the characters consist of printable ascii characters.
"""


class Solution(object):
    def reverse_string(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s = s.reverse()
        # This also works
        # s = s[::-1]


class RecursiveInPlaceSolution:
    def reverse_string(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0, len(s) - 1)

    def reverse(self, s, l, r):
        if l >= r:
            return
        else:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            self.reverse(s, l + 1, r - 1)
