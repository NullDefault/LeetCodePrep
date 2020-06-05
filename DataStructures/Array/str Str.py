"""
~Implement strStr().

~Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


class SolutionIWrote:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        elif len(haystack) == 1 and len(needle) == 1:
            if haystack == needle:
                return 0
            else:
                return -1

        for i in range(0, len(haystack)):
            if needle == haystack[i:i + len(needle)]:
                return i

        return -1


class SolutionThatsObjectivelyBetter:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
