def valid_line(row):
    nums = set()
    for n in row:
        if n in nums:
            return False
        nums.add(n)

def valid_3x3(x, y, board):
    nums = set()
    for i in range(3):
        for j in range(3):
            if board[x+i][y+j] in nums:
                return False
            nums.add(board[x+i][y+j])

def isvalid_sudoku(board):

    for row_num in range(9):
        if valid_line(board[row_num]) == False:
            return False
    
    for col_num in range(9):
        col = []
        for i in range(9):
            col.append(board[i][col_num])
        if valid_line(board[row_num]) == False:
            return False

    for i in range(0,9,3):
        for j in range(0,9,3):
            if valid_3x3(i, j, board) == False:
                return False
    
    return False
        
    
    
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

isvalid_sudoku(board)

