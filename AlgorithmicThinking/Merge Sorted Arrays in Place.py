"""
~Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

~Note:

    ~The number of elements initialized in nums1 and nums2 are m and n respectively.
    ~You may assume that nums1 has enough space (size that is greater or equal to m + n)
        to hold additional elements from nums2.
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        d = {}

        i1, i2, ii = 0, 0, 0

        while i1 < m and i2 < n:

            c1 = nums1[i1] if ii <= i1 else d[i1]
            c2 = nums2[i2]

            if c1 <= c2:
                if ii > i1:
                    d[ii] = nums1[ii]
                    nums1[ii] = c1
                else:  # ii <= i1
                    nums1[ii] = c1
                i1 = i1 + 1
            else:
                if ii >= i1:
                    d[ii] = nums1[ii]
                    nums1[ii] = c2
                else:
                    nums1[ii] = c2
                i2 = i2 + 1

            ii = ii + 1

        if i1 >= m:
            while i2 < n:
                nums1[ii] = nums2[i2]
                ii = ii + 1
                i2 = i2 + 1

        elif i2 >= n:
            while i1 < m:
                c1 = nums1[i1] if ii <= i1 else d[i1]
                if ii > i1:
                    d[ii] = nums1[ii]
                    nums1[ii] = c1
                else:  # ii <= i1
                    nums1[ii] = c1
                i1 = i1 + 1
                ii = ii + 1


class CheekyAssholeSolution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j = 0
        for i in range(m, len(nums1)):
            nums1[i] = nums2[j]
            j += 1
        nums1.sort()
