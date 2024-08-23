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
        depths = map(self.maxDepth, [root.left, root.right])
        return max(depths) + 1
    
    # one line
    # return max(map(self.maxDepth, [root.left, root.right])) + 1 if root else 0