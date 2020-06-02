"""
~Given two arrays, write a function to compute their intersection.
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        def count_nums(arr):
            d = {}
            for n in arr:
                if d.get(n) is None:
                    d[n] = 1
                else:
                    d[n] += 1
            return d

        a1, a2 = count_nums(nums1), count_nums(nums2)

        ans = []
        for key in a1.keys():
            if a2.get(key) is not None:
                count = a1[key] if a1[key] < a2[key] else a2[key]
                for i in range(0, count):
                    ans.append(key)
        return ans
