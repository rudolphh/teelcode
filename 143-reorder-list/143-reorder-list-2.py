from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle of the list
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # reverse the second half
        second = slow.next
        prev = slow.next = None
        while second:
            second.next, prev, second = prev, second, second.next

        first = head
        second = prev
        # merge the two lists
        while first and second:
            first.next, second.next, second, first = second, first.next, second.next, first.next
