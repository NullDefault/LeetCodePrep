"""
~Given two strings s and t , write a function to determine if t is an anagram of s.
"""


class Solution(object):
    def is_anagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {}
        t_dict = {}

        for c in s:
            if s_dict.get(c) is None:
                s_dict[c] = 1
            else:
                s_dict[c] += 1

        for c in t:
            if t_dict.get(c) is None:
                t_dict[c] = 1
            else:
                t_dict[c] += 1

        return s_dict == t_dict
