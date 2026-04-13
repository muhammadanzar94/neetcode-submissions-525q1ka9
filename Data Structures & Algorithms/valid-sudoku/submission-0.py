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
                        print(vals[i])
                        print(vals[j])
                        print("i", i)
                        print("j", j)
                        print("row_nos[i]", row_nos[i])
                        print("col_nos[i]", col_nos[i])
                        print("row_nos[j]", row_nos[j])
                        print("col_nos[j]", col_nos[j])
                        print("j", j)
                        return False

        return True

            








        # print("row_nos:",row_nos)
        # print("col_nos:",col_nos)
        # print("vals:",vals)
