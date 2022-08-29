puzzle = [
    [3, 9, -1, -1, 5, -1, -1, -1, -1],
    [-1, -1, -1, 2, -1, -1, -1, -1, 5],
    [-1, -1, -1, 7, 1, 9, -1, 8, -1],
    [-1, 5, -1, -1, 6, 8, -1, -1, -1],
    [2, -1, 6, -1, -1, 3, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, 4],
    [5, -1, -1, -1, -1, -1, -1, -1, -1],
    [6, 7, -1, 1, -1, 5, -1, 4, -1],
    [1, -1, 9, -1, -1, -1, 2, -1, -1],
]

def getNextEmpty(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row, col

    return None, None  # if no spaces in the puzzle are empty (-1)

def isValid(puzzle, row, col, value):

    # check 3x3 area
    rowStart = (row // 3) *3
    colStart = (col // 3) *3
    for localRow in range(3):
        for localCol in range(3):
            if value == puzzle[localRow + rowStart][localCol + colStart]:
                return False
    
    # check row
    if value in puzzle[row]:
        return False

    # check collum
    for i in puzzle:
        if i[col] == value:
            return False
    
    return True



def solveSudoku(puzzle):
    row, col = getNextEmpty(puzzle)

    # no more empty cells, puzzle solved
    if row is None:
        return True
    
    # try every number on this cell
    for value in range(1, 10):
        
        # check if the value is valid
        if isValid(puzzle, row, col, value):
            puzzle[row][col] = value

            # solve rest of the puzzle 
            if solveSudoku(puzzle):
                return True
        
        puzzle[row][col] = -1
        
    # could not find any valid number, try different nubmers on previus cells
    return False
        
solveSudoku(puzzle)
print(puzzle)