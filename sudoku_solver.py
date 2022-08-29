import sys
import threading
from PyQt6.QtWidgets import QApplication
from window import Window
from solver import Solver

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


def exit_app(sudoku_solver, solver_thread):
    sudoku_solver.is_force_exit = True
    solver_thread.join()
    sys.exit(0)


if __name__ == "__main__":
    # create window
    app = QApplication(sys.argv)
    window = Window(example_puzzle)
    window.show()

    solver = Solver()

    # create a new thread and solve sudoku
    thread = threading.Thread(target=solver.solve_sudoku, args=(example_puzzle, window,))
    thread.start()

    # close solver thread if quiting the app before solution was found
    app.aboutToQuit.connect(lambda: exit_app(solver, thread))

    # run Qt app
    sys.exit(app.exec())
