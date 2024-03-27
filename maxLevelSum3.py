# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # idea: go through the tree and associate each node with its level.
        #.      then go through the tree and have a array where index i is the total
        #       sum for that level. Finally find the array index with the max value

        levelTable = {}
        self.maxLevelSumHelper(root, levelTable, 1)
        levelSumArr = [0]
        self.maxLevelSummer(root, levelTable, levelSumArr)
        currMax = root.val
        maxLevel = 1
        currInd = 0
        for ele in levelSumArr:
            if (currInd == 0):
                currInd += 1
                continue
            if ele > currMax:
                currMax = ele
                maxLevel = currInd
            currInd += 1
        return maxLevel
            

    def maxLevelSumHelper(self, root, levelTable, currLevel):
        if (root != None):
            levelTable[root] = currLevel
            self.maxLevelSumHelper(root.left, levelTable, currLevel+1)
            self.maxLevelSumHelper(root.right, levelTable, currLevel+1)
    
    def maxLevelSummer(self, root, levelTable, levelSumArr):
        if (root == None):
            return
        if len(levelSumArr) <= levelTable[root]:
            levelSumArr.append(root.val)
        else:
            levelSumArr[levelTable[root]] += root.val
        self.maxLevelSummer(root.left, levelTable, levelSumArr)
        self.maxLevelSummer(root.right, levelTable, levelSumArr)
