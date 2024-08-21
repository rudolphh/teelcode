

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        def inOrder(node):
            return inOrder(node.left) + [node.val] + inOrder(node.right) if node else []

        return inOrder(root)[k-1]