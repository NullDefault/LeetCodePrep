"""
~Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
"""


class Solution(object):
    def first_uniq_char(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = []
        seen_stack = []

        for i in range(0, len(s)):
            c = s[i]
            if c in seen_stack:
                pass
            elif c in stack:
                stack.pop(stack.index(c))
                seen_stack.append(c)
            else:
                stack.append(c)

        if len(stack) == 0:
            return -1
        else:
            return s.index(stack[0])


class CleanSolution:
    def first_uniq_char(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)

        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1
