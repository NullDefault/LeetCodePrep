"""
~Merge two sorted linked lists and return it as a new sorted list.
~The new list should be made by splicing together the nodes of the first two lists.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class IterativeSolution:
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Empty List Edge Cases
        if l1 is None:
            if l2 is not None:
                return l2
            else:
                return None
        if l2 is None:
            # We already know l1 is not None so we can return it
            return l1

        head, a, b = (l1, l1.next, l2) if l1.val <= l2.val else (l2, l1, l2.next)

        if a is None:
            head.next = b
            return head
        elif b is None:
            head.next = a
            return head

        curr = head
        while True:
            if a.val <= b.val:
                curr.next = a
                curr = a
                a = a.next
            else:
                curr.next = b
                curr = b
                b = b.next

            if a is None:
                curr.next = b
                break
            elif b is None:
                curr.next = a
                break

        return head


class SexyRecursiveSolution:
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1

        if l1.val <= l2.val:
            l1.next = self.merge_two_lists(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_lists(l1, l2.next)
            return l2

