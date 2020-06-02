"""
~Given an array nums, write a function to move all 0's to the end of it
          while maintaining the relative order of the non-zero elements.
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        offset = 0
        # Iterate through the array, counting zeroes and inserting non-zeroes at the head when necessary.
        for i in range(0, len(nums)):
            if nums[i] == 0:
                zero_count += 1
            else:
                nums.insert(0 + offset, nums[i])
                offset += 1
                nums.pop(i)
        # Insert the appropriate number of zeroes at the end of the array
        for j in range(len(nums) - 1, len(nums) - 1 - zero_count, -1):
            nums[j] = 0


# This is the optimized 2 pointer approach. Accomplishes the same in considerably less number of operations.
class Solution2(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        insert_at = 0
        zero_count = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[insert_at] = nums[i]
                insert_at += 1
            else:
                zero_count += 1
        while zero_count > 0:
            nums[len(nums) - zero_count] = 0
            zero_count -= 1
