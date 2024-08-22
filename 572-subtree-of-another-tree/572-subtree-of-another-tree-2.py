from typing import Optional
from collections import deque
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
        
        def sameTree(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                if node.val == subRoot.val:
                    if sameTree(node, subRoot):
                        return True
                q.append(node.left)
                q.append(node.right)

        return False



def main():
    root = build_tree([3, 4, 5, 1, 2, None, None, None, None, 1, None])
    subroot = build_tree([4, 1, 2])

    print("Subroot is a subtree of root: ", end=' ')
    print(Solution().isSubtree(root, subroot))


if __name__ == '__main__':
    main()