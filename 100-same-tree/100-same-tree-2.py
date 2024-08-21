from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def check(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False

            return True

        que = deque([(p, q)])

        while que:
            p, q = que.popleft()

            if not check(p, q):
                return False
            if p:
                que.append((p.left, q.left))
                que.append((p.right, q.right))


        return True
