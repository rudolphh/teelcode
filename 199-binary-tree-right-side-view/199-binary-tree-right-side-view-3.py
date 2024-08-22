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
            return root
        rsv = []
        q = deque([root])
        while q:
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if i == 0:
                    rsv.append(node.val)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

        return rsv

                
                
        