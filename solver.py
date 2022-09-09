import sys
import time


class Solver:

    speed = 1
    is_force_exit = False
    is_solved = False

    def __init__(self, finish_callback):
        self.finish_callback = finish_callback

    def solve_sudoku(self, puzzle, window):
        row, col = self.__get_next_empty(puzzle)

        # no more empty cells, puzzle solved
        if row is None:
            self.finish_callback()
            self.is_solved = True
            sys.exit()

        # try every number on this cell
        for value in range(1, 10):
            # check if the user closed the app
            if self.is_force_exit:
                sys.exit()

            # check if the value is valid
            if self.is_valid(puzzle, row, col, value):
                puzzle[row][col] = value

                # update window
                window.UpdateGridSignal.emit(puzzle)
                # time.sleep(0.1 / self.speed)

                # solve rest of the puzzle
                if self.solve_sudoku(puzzle, window):
                    return True

            puzzle[row][col] = -1

        # could not find any valid number, try different numbers on previous cells
        return False

    def __get_next_empty(self, puzzle):
        for row in range(9):
            for col in range(9):
                if puzzle[row][col] == -1:
                    return row, col

        return None, None  # if no cells in the puzzle are empty (-1)

    def is_valid(self, puzzle, row, col, value):
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
