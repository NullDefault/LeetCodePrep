"""
~Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

~For this problem, a height-balanced binary tree is defined as a binary tree
    in which the depth of the two subtrees of every node never differ by more than 1.
"""


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        n = len(nums)
        root = TreeNode(nums[n // 2])

        if n == 1:
            return root
        else:
            root.left = self.sortedArrayToBST(nums[:n // 2])
            root.right = self.sortedArrayToBST(nums[n // 2 + 1:])
        return root
