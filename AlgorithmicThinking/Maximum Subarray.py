"""
~Given an integer array nums, find the contiguous subarray (containing at least one number)
    which has the largest sum and return its sum.
"""


class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        abs_max = nums[0]
        curr_max = nums[0]
        for i in range(1, len(nums)):
            curr_max = max(nums[i], curr_max + nums[i])
            abs_max = max(curr_max, abs_max)
        return abs_max
