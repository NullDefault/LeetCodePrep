"""
~Given a singly linked list, determine if it is a palindrome.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class SuboptimalSolution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        if head.next is None:
            return True

        stack = []
        while head is not None:
            stack.append(head.val)
            head = head.next

        return stack == stack[::-1]

    """
    The best solution (one that uses O(1) space and O(n) time) is possible using a complicated multi pointer approach.
    Essentially, the algorithm is as follows
        1) Get to middle of the linked list (this is what we use the slow and fast pointer for)
        2) Reverse everything after the middle (one complicated aspect of this approach is the fact that we have to
         know if we are dealing with an even or odd linked list, keeping track of the middle element in the latter case)
        3) Starting from the two heads (first half in the original order and second reversed), compare the two lists
         and see if they are the same. If they are, return true. Otherwise false.
    """
