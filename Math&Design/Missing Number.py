"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
"""


def missing_number(nums) -> int:
    nums_sum = sum(nums)
    true_sum = sum(range(0, len(nums)+1))
    return true_sum - nums_sum

