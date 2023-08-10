class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        # Idea: use recursion with 4 arrays to indicate whether the previous row/col was X or O

        prevTopRow = []
        prevBotRow = []
        prevLeftCol = []
        prevRightCol = []
        for _ in range(len(board)):
            prevTopRow.append(0)
            prevBotRow.append(0)
        for _ in range(len(board[0])):
            prevLeftCol.append(0)
            prevRightCol.append(0)

        self.solveHelper(board, prevTopRow, prevBotRow, prevLeftCol, PrevRightCol)
    
    def solveHelper(self, board, prevTopRow, prevBotRow, prevLeftCol, PrevRightCol):
        if len(board) == 0:
            return
        
