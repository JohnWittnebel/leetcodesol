# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # idea: observe an interior node. The optimal path that traverses this node will
        #       go through the parent and left/right node, or go through right+left node.
        #.      We can recursively find the best path at each subtree that uses left/right node.
        #       Then we find the subtree that has the largest left+right path and we are done.

        rootMaxPath = self.setMaxPathDescends(root)
        return self.findMaxPath(root)

    
    def setMaxPathDescends(self, root):
        if root == None:
            return 0
        leftMax = self.setMaxPathDescends(root.left)
        rightMax = self.setMaxPathDescends(root.right)
        root.leftMax = leftMax + root.val
        root.rightMax = rightMax + root.val
        return root.val + max(leftMax, rightMax, 0)
    
    def findMaxPath(self, root):
        if root.left == None and root.right == None:
            return root.val
        if root.left == None:
            maxRight = self.findMaxPath(root.right)
            return max(maxRight, root.rightMax, root.leftMax)
        if root.right == None:
            maxLeft = self.findMaxPath(root.left)
            return max(maxLeft, root.leftMax, root.rightMax)
        maxLeft = self.findMaxPath(root.left)
        maxRight = self.findMaxPath(root.right)
        return max(maxLeft, maxRight, root.leftMax+root.rightMax-root.val, root.val, root.leftMax, root.rightMax)

