class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # Base Case:
        if rowIndex == 0:
            return [1]
        
        # Recursive call
        prevRow = self.getRow(rowIndex - 1)
        currIndex = 0
        n = len(prevRow)
        newRow = [1]
        while currIndex < n-1:
            newRow.append(prevRow[currIndex] + prevRow[currIndex+1])
            currIndex += 1
        newRow.append(1)
        return newRow

        
