from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # one pass
        dummy = ListNode()
        dummy.next = head

        first = second = dummy
        for _ in range(n + 1):
            first = first.next

        while first:
            first, second = first.next, second.next

        second.next = second.next.next
        
        return dummy.next
        