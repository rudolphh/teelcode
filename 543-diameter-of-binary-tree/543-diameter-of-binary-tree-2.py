from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        l_path = [0]
        def longest_path(node):
            if not node:
                return 0

            LP = longest_path(node.left)
            RP = longest_path(node.right)

            # process the information we have about left and right paths
            # at the current node
            l_path[0] = max(l_path[0], LP + RP)

            return max(LP, RP) + 1

        longest_path(root)
        return l_path[0]
    
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