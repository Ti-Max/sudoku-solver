def get_next_empty(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row, col

    return None, None  # if no spaces in the puzzle are empty (-1)


def is_valid(puzzle, row, col, value):

    # check 3x3 area
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for localRow in range(3):
        for localCol in range(3):
            if value == puzzle[localRow + row_start][localCol + col_start]:
                return False
    
    # check row
    if value in puzzle[row]:
        return False

    # check column
    for i in puzzle:
        if i[col] == value:
            return False
    
    return True


def solve_sudoku(puzzle):
    row, col = get_next_empty(puzzle)

    # no more empty cells, puzzle solved
    if row is None:
        return True
    
    # try every number on this cell
    for value in range(1, 10):
        
        # check if the value is valid
        if is_valid(puzzle, row, col, value):
            puzzle[row][col] = value

            # solve rest of the puzzle 
            if solve_sudoku(puzzle):
                return True
        
        puzzle[row][col] = -1
        
    # could not find any valid number, try different numbers on previous cells
    return False


example_puzzle = [
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
solve_sudoku(example_puzzle)
print(example_puzzle)
