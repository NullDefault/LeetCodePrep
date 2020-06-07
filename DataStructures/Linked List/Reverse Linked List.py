"""
~Reverse a singly linked list.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class IterativeSolution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        last_node = None
        node = head
        while node.next is not None:
            next_node = node.next
            node.next = last_node
            last_node = node
            node = next_node

        node.next = last_node
        return node
