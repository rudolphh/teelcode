from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pass

        # find the length
        length = 0
        dummy = ListNode()
        dummy.next = head
        while head:
            length += 1
            head = head.next

        node_before_nth = dummy
        for _ in range(length-n):
            node_before_nth = node_before_nth.next

        # head is at the node before the nth
        node_before_nth.next = node_before_nth.next.next

        return dummy.next
        