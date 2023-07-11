# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # corner case, otherwise we go to helper that runs the basic recursion
        if root == None:
            return 0
        return self.minDepthHelper(root)
    
    # requires that root != None
    def minDepthHelper(self, root):
        if (root.left == None and root.right == None):
            return 1
        if root.left == None:
            return 1 + self.minDepth(root.right)
        if root.right == None:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
