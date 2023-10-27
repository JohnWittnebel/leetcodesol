# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        sortedList = self.myDFS(root)
        index = 0
        while index < len(sortedList) - 1:
            sortedList[index].left = None
            sortedList[index].right = sortedList[index + 1]
            index += 1
        print(index)

    def myDFS(self, root):
        if root == None:
            return []
        return [root] + self.myDFS(root.left) + self.myDFS(root.right)
