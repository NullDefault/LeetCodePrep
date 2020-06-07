"""
~Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

    ~Note: For the purpose of this problem, we define empty string as valid palindrome.
"""


class Solution(object):
    def is_palindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = []
        for c in s:
            if c.isalpha() or c.isnumeric():
                new_s.append(c.lower())

        return new_s == new_s[::-1]
