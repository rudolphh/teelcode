from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            curr_level_count = len(q)
            curr_level = []
            for i in range(curr_level_count):
                node = q.popleft()

                # process the node
                # can also have no curr_level list and just append the
                # last node in level (i == curr_level_count - 1)
                # or first node if reverse enqueue (right first then left)
                curr_level.append(node.val)

                # enqueue any left and right nodes
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(curr_level[-1])

        return result

                
                
        