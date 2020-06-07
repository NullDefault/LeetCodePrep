"""
~Given a binary tree, find its maximum depth.

~The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

~Note: A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def max_depth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1


class QueueSolution:
    def max_depth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = deque()
        queue.append(root)
        d = 0
        while queue:
            l = len(queue)
            for i in range(l):
                root = queue.popleft()
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            d += 1
        return d
