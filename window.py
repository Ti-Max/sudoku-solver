import threading

from PyQt6.QtWidgets import *
from PyQt6.QtGui import * 
from PyQt6.QtCore import *


class Window(QWidget):
    UpdateGridSignal = pyqtSignal(int)

    def __init__(self, puzzle, start_solving):
        super().__init__()

        # window properties
        self.setWindowTitle("Sudoku solver")
        self.setWindowIcon(QIcon("icon.png"))
        self.setGeometry(360, 360, 360, 360)

        # main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Status message
        self.status_massage = QLabel("Click \"Solve\" to solve sudoku using a backtracking method.", self)
        self.status_massage.setFont(QFont("Roboto", 10))
        self.status_massage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.status_massage)

        # sudoku layout
        sudoku_layout = QHBoxLayout()
        main_layout.addLayout(sudoku_layout)

        # create sudoku grid
        self.grid = QGridLayout()
        sudoku_layout.addLayout(self.grid)
        self.grid.setSpacing(0)

        for row in range(9):
            for col in range(9):
                cell = QLabel("")
                cell.setMinimumSize(40, 40)
                cell.setMaximumSize(40, 40)
                cell.setAlignment(Qt.AlignmentFlag.AlignCenter)
                cell.setFont(QFont('Roboto', 20))

                style = ""

                # make borders thicker on the outside and in between 3x3 squares
                if row == 0:
                    style += "border-top: 3px solid black; border-bottom: 1px solid black;"
                elif row == 2 or row == 5:
                    style += "border-bottom: 3px solid black;"
                elif row == 8:
                    style += "border-bottom: 3px solid black;"
                else:
                    style += "border-bottom: 1px solid black;"

                if col == 0:
                    style += "border-left: 3px solid black; border-right: 1px solid black;"
                elif col == 2 or col == 5:
                    style += "border-right: 3px solid black;"
                elif col == 8:
                    style += "border-right: 3px solid black;"
                else:
                    style += "border-right: 1px solid black;"

                # check pattern
                if ((row < 3 or row > 5) and (col < 3 or col > 5)) or (2 < row < 6 and 2 < col < 6):
                    style += "background-color: #d3edce;"
                else:
                    style += "background-color: #edf7eb;"

                # mark pre-made cells
                if puzzle[row][col] != -1:
                    style += "color: #1ca600;"

                cell.setStyleSheet(style)
                self.grid.addWidget(cell, row, col)

        # create controls
        control_layout = QVBoxLayout()
        sudoku_layout.addLayout(control_layout)

        # solve button
        self.solve_button = QPushButton("Solve")
        control_layout.addWidget(self.solve_button)
        self.solve_button.clicked.connect(start_solving)

        self.UpdateGridSignal.connect(lambda: self.update_sudoku(puzzle))

        # update sudoku
        self.update_sudoku(puzzle)

    def close_window(self):
        self.close()

    def update_sudoku(self, puzzle):
        i = 0
        for row in range(9):
            for col in range(9):
                if puzzle[row][col] == -1:
                    value = ""
                else:
                    value = str(puzzle[row][col])

                self.grid.itemAt(i).widget().setText(value)
                i += 1

    def solve_started(self):
        self.status_massage.setText("Solving sudoku...")
        self.status_massage.setStyleSheet("color: red;")

    def solve_finished(self):
        self.status_massage.setText("Sudoku is solved!")
        self.status_massage.setStyleSheet("color: green;")
