from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def height(root):
            if not root:
                return 0
            
            left = height(root.left)
            right = height(root.right)
            res[0] = max(res[0], left + right)

            return 1 + max(left, right)
        
        height(root)
        return res[0]

    
def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    print(solution.diameterOfBinaryTree(root))


if __name__ == "__main__":
    main()