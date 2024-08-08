from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        
        if not root:
            return []
        lot = []
        queue = deque([root])

        while queue:
            level = []
            level_count = len(queue)

            for _ in range(level_count):
                node = queue.popleft()

                # process node
                level.append(node.val)

                # enqueue left and then right child
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            lot.append(level)

        return lot