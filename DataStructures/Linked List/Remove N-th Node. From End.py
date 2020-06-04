"""
~Given a linked list, remove the n-th node from the end of list and return its head.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        # Edge case if the given list is of size 1
        if head.next is None:
            return None

        d = {}
        i = 0
        node = head
        while True:
            d[i] = node
            node = node.next
            i = i + 1
            if node is None:
                break
        node_to_delete = d[i - n]

        if node_to_delete.next is not None:
            node_to_delete.val = node_to_delete.next.val
            node_to_delete.next = node_to_delete.next.next
        else:
            d[i - n - 1].next = None

        return d[0]
