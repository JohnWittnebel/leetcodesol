# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # we need to check the rightmost node in the left subtree and the leftmost node in the
        # right subtree to verify that all elements in the left subtree are less than the current
        # root, and all elements in the right subtree are greater. This is O(n) time, as we only
        # traverse each node at most 2 times.

        # Base cases
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        
        # Check that all values in right subtree are greater and right subtree is BST
        if root.right != None:
            smallest = self.getSmallest(root.right)
            if (smallest <= root.val):
                return False
            rightBST = self.isValidBST(root.right)
            # minor optimization where if the right side is not a BST we can save a bit of work
            if not rightBST:
                return False

        # Check that all values in the left subtree are smaller and left subtree is BST
        if root.left != None:
            largest = self.getLargest(root.left)
            if (largest >= root.val):
                return False
            leftBST = self.isValidBST(root.left)
            return leftBST
        return True
    
    def getSmallest(self, root):
        if root.left == None:
            return root.val
        else:
            return self.getSmallest(root.left)
    
    def getLargest(self, root):
        if root.right == None:
            return root.val
        else:
            return self.getLargest(root.right)
