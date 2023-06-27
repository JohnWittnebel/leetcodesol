class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # Idea: Use DFS-esque algorithm
        visitedArr = self.zeros(len(board), len(board[0]))

        foundWord = False
        row = 0
        while row < len(board) and not foundWord:
            col = 0
            while col < len(board[0]) and not foundWord:
                if (board[row][col] == word[0]):
                    foundWords = self.myDFS(board, visitedArr, row, col, word[1:])
                    if (foundWords > 0):
                        foundWord = True
                    visitedArr = self.zeros(len(board), len(board[0]))
                col += 1
            row += 1
        
        return foundWord
    
    def myDFS(self, board, visitedArr, row, col, word):
        visitedArr[row][col] = 1

        myVisitCopy = []
        for ele in visitedArr:
            myVisitCopy.append(copy.copy(ele))

        if word == "":
            return 1

        foundWord = 0
        if row != 0:
            if not visitedArr[row - 1][col] and board[row - 1][col] == word[0]:
                foundWord += self.myDFS(board, visitedArr, row-1, col, word[1:])
                visitedArr = myVisitCopy
        if col != 0:
            if not visitedArr[row][col - 1] and board[row][col - 1] == word[0]:
                foundWord += self.myDFS(board, visitedArr, row, col-1, word[1:])
                visitedArr = myVisitCopy
        if row != len(board) - 1:
            if not visitedArr[row + 1][col] and board[row + 1][col] == word[0]:
                foundWord += self.myDFS(board, visitedArr, row+1, col, word[1:])
                visitedArr = myVisitCopy
        if col != len(board[0]) - 1:
            if not visitedArr[row][col + 1] and board[row][col + 1] == word[0]:
                foundWord += self.myDFS(board, visitedArr, row, col+1, word[1:])
                visitedArr = myVisitCopy
        return foundWord


    
    def zeros(self, row, col):
        retArr = []
        for _ in range(row):
            newRow = []
            for _ in range(col):
                newRow.append(False)
            retArr.append(newRow)
        return retArr
            
