# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def is_symmetric(self, root: TreeNode) -> bool:
        return self.does_reflect(root, root)

    def does_reflect(self, a: TreeNode, b: TreeNode):
        if a is None and b is None:
            return True
        elif a is None or b is None:
            return False
        else:
            return a.val == b.val and self.does_reflect(a.right, b.left) and self.does_reflect(a.left, b.right)
