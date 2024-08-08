from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        q = deque([(root, float('-inf'), float('inf'))])

        while q:

            node, low, high = q.popleft()
            if not (low < node.val < high):
                return False 
            
            # enqueue the left and right
            if node.left:
                q.append((node.left, low, node.val))
            if node.right:
                q.append((node.right, node.val, high))

        return True