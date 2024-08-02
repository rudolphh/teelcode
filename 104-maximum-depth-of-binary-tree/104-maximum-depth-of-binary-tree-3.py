from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # initialize the queue
        queue = deque([(root, 1)])
        max_depth = 0

        while queue:
            node, depth = queue.popleft()
            if node:
                max_depth = max(max_depth, depth)
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))


        return max_depth