"""
~You are a product manager and currently leading a team to develop a new product.
    Unfortunately, the latest version of your product fails the quality check.
        Since each version is developed based on the previous version, all the versions after a bad version are also bad

~Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
    which causes all the following ones to be bad.

~You are given an API bool isBadVersion(version) which will return whether version is bad.
    Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

def first_bad_version(n):
    """
    :type n: int
    :rtype: int
    """
    left, right = 1, n
    while left < right:
        mid = (left+right) // 2
        right, left = (mid, left) if isBadVersion(mid) else (right, mid + 1)
    return left

# The two solutions are the same, the one below doesn't use cool one liners tho


def first_bad_version(n):
    """
    :type n: int
    :rtype: int
    """
    left = 1
    right = n

    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left
