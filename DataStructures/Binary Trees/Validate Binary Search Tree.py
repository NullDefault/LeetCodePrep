"""
~Given a binary tree, determine if it is a valid binary search tree (BST).

~Assume a BST is defined as follows:

    ~The left subtree of a node contains only nodes with keys less than the node's key.
    ~The right subtree of a node contains only nodes with keys greater than the node's key.
    ~Both the left and right subtrees must also be binary search trees.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def is_valid_bst(self, root: TreeNode, minNode=None, maxNode=None) -> bool:
        if root is None:
            return True
        elif minNode and root.val >= minNode.val:
            return False
        elif maxNode and root.val <= maxNode.val:
            return False
        else:
            return self.is_valid_bst(root.left, minNode=root, maxNode=maxNode) \
                   and self.is_valid_bst(root.right, minNode=minNode, maxNode=root)
