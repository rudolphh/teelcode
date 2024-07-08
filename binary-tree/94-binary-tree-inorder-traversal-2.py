# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        current = root

        # this will traverse every new right node
        # treat root like a new right node
        while current is not None or stack:
            # while there are more left nodes
            while current is not None:
                stack.append(current)  # add to the stack
                current = current.left  # traverse left

            # current is now None, so pop it back to last left node
            current = stack.pop()
            # this is the next in order node so add to results
            result.append(current.val)
            # traverse the right side of the last left
            current = current.right


        return result