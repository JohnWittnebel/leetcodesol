class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        transposed = []
        for i in range(len(grid)):
            newrow = []
            for j in range(len(grid)):
                newrow.append(grid[j][i])
            transposed.append(newrow)
        
        retVal = 0
        for ele in grid:
            for transEle in transposed:
                if ele == transEle:
                    retVal += 1
        return retVal
