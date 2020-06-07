"""
~Given an array of integers, return indices of the two numbers such that they add up to a specific target.

~You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""


class Solution(object):
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        for i in range(0, len(nums)):
            existing_index = table.get(nums[i])
            if existing_index is None:
                table[nums[i]] = i
            else:
                if nums[i] * 2 == target:
                    return existing_index, i
        for key in table:
            if table.get(target - key) is not None:
                return table[key], table[target-key]
