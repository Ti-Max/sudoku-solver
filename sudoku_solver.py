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


def exit_app():
    solver.is_force_exit = True
    if solver_thread.is_alive():
        solver_thread.join()
    sys.exit(0)


def start_solving():
    if not solver_thread.is_alive():
        solver_thread.start()


if __name__ == "__main__":
    # create window
    app = QApplication(sys.argv)

    solver = Solver()

    window = Window(example_puzzle, start_solving)
    window.show()

    # create a new thread which will solve sudoku
    solver_thread = threading.Thread(target=solver.solve_sudoku, args=(example_puzzle, window,))

    # close solver thread if quiting the app before solution was found
    app.aboutToQuit.connect(exit_app)

    # run Qt app
    sys.exit(app.exec())
