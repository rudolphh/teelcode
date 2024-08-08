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
    def goodNodes(self, root: TreeNode) -> int:
        good = []

        def dfsPathMax(root, max_val):
            if not root:
                return

            if root.val >= max_val:
                good.append(root.val)

            dfsPathMax(root.left, root.val if root.val >= max_val else max_val)
            dfsPathMax(root.right, root.val if root.val >= max_val else max_val)


        dfsPathMax(root, root.val)
        #print(good)
        return len(good)
    

def main():
    root = build_tree([3,1,4,3,None,1,5])
    s = Solution()
    print(s.goodNodes(root))

if __name__ == "__main__":
    main()

