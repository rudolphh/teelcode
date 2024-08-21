from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        stack = [root]
        depth = {}
        visit_stack = []

        l_path = 0

        while stack:
            node = stack.pop()
            if node:
                visit_stack.append(node)
                stack.append(node.left)
                stack.append(node.right)

        while visit_stack:

            node = visit_stack.pop()

            LP = depth.get(node.left, 0)
            RP = depth.get(node.right, 0)

            l_path = max(l_path, LP + RP)

            depth[node] = max(LP, RP) + 1


        return l_path
    
    
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