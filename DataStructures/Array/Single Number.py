"""
~Given a non-empty array of integers, every element appears twice except for one. Find that single one.

~Note:
    ~Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

# This is the solution I came up with myself. It gets the answer in O(n), but it uses extra space since I couldn't
# figure out how to avoid that.


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = {}

        for el in nums:
            try:
                if ans[el]:
                    ans[el] += 1
            except:
                ans[el] = 1

        for el in ans:
            if ans[el] == 1:
                return el


# This is the big brain bit manipulation solution. Below is an explanation of how it works.
"""
If we take XOR of zero and some bit, it will return that bit
If we take XOR of two same bits, it will return 0
So we can XOR all bits together to find the unique number.
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            # As far as I understand it, the line below takes the XOR of all bits together, which eventually lets us
            # find the answer since it is going to be the only bit that doesnt return 0.
            a ^= i
        return a
