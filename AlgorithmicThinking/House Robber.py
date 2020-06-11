"""
~You are a professional robber planning to rob houses along a street.
    Each house has a certain amount of money stashed, the only constraint stopping you
    from robbing each of them is that adjacent houses have security system connected and it will automatically contact
    the police if two adjacent houses were broken into on the same night.

~Given a list of non-negative integers representing the amount of money of each house,
    determine the maximum amount of money you can rob tonight without alerting the police.
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            h1 = nums[0]
            h2 = nums[1] if nums[1] > nums[0] else nums[0]
            for i in range(2, len(nums)):
                temp = max(h2, h1+nums[i])
                h1 = h2
                h2 = temp
            return h2
