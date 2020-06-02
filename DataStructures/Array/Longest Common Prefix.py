class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        i = 0
        done = False
        while not done:
            try:
                next_char = strs[0][i]
                for j in range(1, len(strs)):
                    if next_char != strs[j][i]:
                        done = True
                if not done:
                    prefix = prefix + next_char
            except IndexError:  # if we get an index out of bounds error we exit out of the loop
                done = True
            i = i + 1
        return prefix
