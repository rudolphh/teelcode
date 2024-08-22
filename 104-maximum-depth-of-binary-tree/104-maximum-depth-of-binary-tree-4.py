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

        stack = [root]
        visited_order = []

        while stack:
            node = stack.pop()
            if node:
                visited_order.append(node)
                stack.append(node.right)
                stack.append(node.left)

        depth = {}
        max_depth = 0

        while visited_order:
            node = visited_order.pop()

            left = depth.get(node.left, 0)
            right = depth.get(node.right, 0)

            depth[node] = max(left, right) + 1

            max_depth = max(depth[node], max_depth)

        return max_depth