"""
~Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

    (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

~You are given a target value to search. If found in the array return its index, otherwise return -1.

~You may assume no duplicate exists in the array.

~Your algorithm's runtime complexity must be in the order of O(log n).
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[0] <= target <= nums[m] or target <= nums[m] < nums[0] or nums[m] < nums[0] <= target:
                r = m - 1
            else:
                l = m + 1
        return -1
    