# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        # Base Case, we are went down the empty side of a path
        if (root == None):
            return None

        # Base Case, we are at a leaf
        if (root.left == None and root.right == None):
            if root.val == targetSum:
                return [[root.val]]
            else:
                return None

        # Recursive calls
        leftPaths = self.pathSum(root.left, targetSum - root.val)
        rightPaths = self.pathSum(root.right, targetSum - root.val)

        retVal = []
        if leftPaths != None:
            for path in leftPaths:
                retVal.append([root.val] + path)
        if rightPaths != None:
            for path in rightPaths:
                retVal.append([root.val] + path)
    
        return retVal
