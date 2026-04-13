class Solution:
    def faultFound(self, r1: int, c1: int, r2: int, c2: int) -> bool:
        if(r1 == r2):
            return True
        elif(c1 == c2):
            return True
        elif(abs(r2-r1)<=2 and abs(c2-c1)<=2):
            if((r1//3)*3+(c1//3) == (r2//3)*3+(c2//3)): # if same square
                return True
        else:
            return False

    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = len(board)

        row_nos = []
        col_nos = []
        vals = []

        for i in range(n):
            for j in range(n):

                if(board[i][j] != "."):
                    row_nos.append(i)
                    col_nos.append(j)
                    vals.append(board[i][j])
        
        val_n = len(vals)

        for i in range(val_n):
            for j in range(i+1, val_n):
                if(vals[i] == vals[j]):
                    if(self.faultFound(row_nos[i], col_nos[i], row_nos[j], col_nos[j]) == True):
                        return False

        return True