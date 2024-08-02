from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(tree: list = []):
    
    if tree:
        tree.reverse()
        root = TreeNode(tree.pop())
    else:
        return
    
    curr_head = root
    prev_head = root
    left_next = True
    
    while tree:
        node_val = tree.pop()
        if node_val:
            curr_head.left = TreeNode(node_val)
            next_head = curr_head.left
        node_val = tree.pop()
        if node_val:
            curr_head.right = TreeNode(node_val)

        if left_next:
            prev_head = curr_head
            curr_head = next_head
            left_next = False
        else:
            curr_head = prev_head.right
            left_next = True

    return root

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        res = [0]

        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)

            res[0] = max(res[0], abs(left_height - right_height))
            
            # Return the height of the current node
            return 1 + max(left_height, right_height)

        height(root)
        return res[0] <= 1
    


def main():
    head = buildTree([3, 9, 20, None, None, 15, 17])

    solution = Solution()
    print(solution.isBalanced(head))
    print(solution.isBalanced(buildTree([1,2,2,3,3,None,None,4,4])))
    print(solution.isBalanced(buildTree([])))
    print(solution.isBalanced(buildTree([1])))




if __name__ == "__main__":
    main()