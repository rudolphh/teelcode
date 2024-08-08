from typing import Optional
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helper_modules.trees import build_tree 


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            return False

        def sameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

            if not p and not q:
                return True

            if not p or not q or p.val != q.val:
                return False

            same_left = sameTree(p.left, q.left)
            same_right = sameTree(p.right, q.right)

            return same_left and same_right

        if sameTree(root, subRoot):
            return True
        else:
            return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))



def main():
    root = build_tree([3, 4, 5, 1, 2, None, None, None, None, 1, None])
    subroot = build_tree([4, 1, 2])

    print("Subroot is a subtree of root: ", end=' ')
    print(Solution().isSubtree(root, subroot))


if __name__ == '__main__':
    main()