# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        # idea: use recursion, takes O(n) time

        # Base cases:
        if root == None:
            return False
        if root.left == None and root.right == None:
            return root.val == targetSum

        leftPathExists = self.hasPathSum(root.left, targetSum - root.val)
        rightPathExists = self.hasPathSum(root.right, targetSum - root.val)
        return leftPathExists or rightPathExists
        
