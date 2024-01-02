import numpy
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        distanceGrid = numpy.zeros((len(obstacleGrid), len(obstacleGrid[0])))
        row = len(obstacleGrid) - 1
        col = len(obstacleGrid[0]) - 2
        if obstacleGrid[row][col+1] == 1:
            return 0
        distanceGrid[row][col+1] = 1
        while row >= 0:
            while col >= 0:
                if obstacleGrid[row][col] == 1:
                    distanceGrid[row][col] = 0
                    col -= 1
                    continue
                if col == len(obstacleGrid[0]) - 1:
                    distanceGrid[row][col] = distanceGrid[row+1][col]
                elif row == len(obstacleGrid) - 1:
                    distanceGrid[row][col] = distanceGrid[row][col+1]
                else:
                    distanceGrid[row][col] = distanceGrid[row][col+1] + distanceGrid[row+1][col]
                col -= 1
            col = len(obstacleGrid[0]) - 1
            row -= 1
        return int(distanceGrid[0][0])

