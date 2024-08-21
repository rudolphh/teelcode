from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        prev = [float('-inf')]

        def inOrder(node):
            if not node:
                return True

            left = inOrder(node.left)

            if node.val <= prev[0]:
                return False

            prev[0] = node.val

            right = inOrder(node.right)

            return left and right

        return inOrder(root)