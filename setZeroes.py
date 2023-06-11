class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Idea: we cant use additional space, and there is a problem that if we start
        #       turning 1's into 0's immediately we might not be able to distinguish
        #       between the original 0's (that require us to do work) and 1's that have
        #       been transformed into 0 (that don't require work). To resolve this,
        #       we will initially transform 1's that should become 0 into 2 until we are
        #       done, then turn all 2's into 0.

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    for k in range(len(matrix[i])):
                        if (matrix[i][k] != 0):
                            matrix[i][k] = 'a'
                    for k in range(len(matrix)):
                        if (matrix[k][j] != 0):
                            matrix[k][j] = 'a'
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0
