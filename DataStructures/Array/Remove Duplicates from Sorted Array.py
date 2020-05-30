"""
~Given a sorted array nums, remove the duplicates in-place
    such that each element appear only once and return the new length.
~Do not allocate extra space for another array,
    you must do this by modifying the input array in-place with O(1) extra memory.
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        elif len(nums) == 2:
            if nums[0] == nums[1]:
                nums = nums[:1]
                return 1
            else:
                return 2

        saved_index = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[saved_index]:
                nums[saved_index] = 'X'
            saved_index = i
        while 'X' in nums:
            nums.remove('X')
        return len(nums)
