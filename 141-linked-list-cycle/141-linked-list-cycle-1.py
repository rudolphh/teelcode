# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # This solution is O(n) but is also O(n) memory because of the hashset
        node_set = set()
        while head:
            if head in node_set:
                return True
            node_set.add(head)

            head = head.next

        return False
        
