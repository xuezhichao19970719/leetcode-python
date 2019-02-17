class Solution:
    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(unit) == len(set(unit))
        
    def isValidSudoku(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False
        a = (0, 3, 6)
        for i in a:
            for j in a:
                s = [board[x][y] for x in (i,i+1,i+2) for y in (j,j+1,j+2)]
                if not self.is_unit_valid(s):
                    return False
        return True