"""
~A peak element is an element that is greater than its neighbors.

~Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

~The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

~You may imagine that nums[-1] = nums[n] = -∞.
"""


class Solution:
    def find_peak_element(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        if l == r:
            return l

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[m + 1]:
                # .  <- m
                #  \
                #   . <- m + 1
                # So we want to search left of m
                r = m
            else:
                #   . <- m + 1
                #  /
                # . <- m
                # So we want to search right of m
                l = m + 1
        return l
