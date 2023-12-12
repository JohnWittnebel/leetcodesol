# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        outArr = []
        myQueue = [[root,0]]
        if root == None:
            return []
        while myQueue:
            nextEle = myQueue.pop(0)
            while len(outArr) <= nextEle[1]:
                outArr.append([])
            outArr[nextEle[1]].append(nextEle[0].val)
            if (nextEle[0].left):
                myQueue.append([nextEle[0].left, nextEle[1] + 1])
            if (nextEle[0].right):
                myQueue.append([nextEle[0].right, nextEle[1] + 1])
        
        return outArr

