"""
~Given an array, rotate the array to the right by k steps, where k is non-negative.

~Follow up:
    Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
    Could you do it in-place with O(1) extra space?

"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        """
        Personal note: spent a while trying to figure this one out but had to resort to studying the solution in the
        end. Although I came up with the brute force and extra space solutions, i couldn't figure out how to implement
        my idea for the in place algorithm. I had the right idea for maintaining cycles between the indexes but couldn't
        write code that worked for all the test cases.
        Here are some lessons learned in this one:
        1) Whenever you are doing any cyclic transformation you can reduce the work by applying modulus onto the passed
        step parameter. For example, here since sometimes rotations will be repeated (i,e a rotation of k=3 on an array
        of size 2 is really just a rotation of k=1) you can do k%=n to avoid problems.
        2) Python for loops are simple so hard to manipulate the way you would in lower level languages. A solid 
        alternative is creating a custom loop through using While in combination with variables that act in place
        of the loop index.
        3) When dealing with cyclic transformations instead of doing this:
                    if inQ >= len(nums):
                        inQ -= len(nums)
           Just do this:
                    inQ = (current + k) % n
           Effectively, %'n by the size of the array will wrap the index around from the other end.
        """

        # N: Size of the array
        n = len(nums)
        # k: rotations necessary. We mod it by n to avoid repeating work.
        k %= n

        start = count = 0

        # ~ While we have seen less elements than are in the array
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                if start == current:
                    break
            start += 1
