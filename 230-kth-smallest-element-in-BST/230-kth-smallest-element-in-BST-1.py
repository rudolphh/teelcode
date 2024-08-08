

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        k_vals = []

        def dfs_smallest(root):
            if not root:
                return

            dfs_smallest(root.left)

            # next smallest value here
            k_vals.append(root.val)

            if len(k_vals) == k:
                return

            dfs_smallest(root.right)

        dfs_smallest(root)

        return k_vals[k-1]