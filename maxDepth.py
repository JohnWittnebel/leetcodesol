# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Idea: the max depth is the larger of the depth of the left and right side, plus 1
        #       simple recursion will solve this

        if root == None:
            return 0
        else:
            leftDepth = self.maxDepth(root.left)
            rightDepth = self.maxDepth(root.right)
            if leftDepth >= rightDepth:
                return leftDepth + 1
            else:
                return rightDepth + 1
