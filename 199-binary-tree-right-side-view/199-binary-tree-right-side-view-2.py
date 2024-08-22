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

        def dfs(node, level):
            if level == len(rsv):
                rsv.append(node.val)
            if node.right:
                dfs(node.right, level + 1)
            if node.left:
                dfs(node.left, level + 1)

        dfs(root, 0)
        return rsv

                
                
        