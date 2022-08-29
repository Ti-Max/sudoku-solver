from PyQt6.QtWidgets import *
from PyQt6.QtGui import * 
from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self, puzzle):
        super().__init__()

        # window properties
        self.setWindowTitle("Sudoku solver")
        self.setWindowIcon(QIcon("icon.png"))
        self.setGeometry(360, 360, 360, 360)

        # main layout
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # create sudoku grid
        self.grid = QGridLayout()
        main_layout.addLayout(self.grid)
        self.grid.setSpacing(0)

        for row in range(9):
            for col in range(9):
                cell = QLabel(str(row))
                cell.resize(40, 40)
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
