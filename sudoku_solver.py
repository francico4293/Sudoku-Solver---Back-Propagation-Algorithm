# Author: Colin Francis
# Date: 6/8/2021
# Description: A more efficient back propagation algorithm to solve Sudoku puzzles

class SolveSudoku(object):
    def __init__(self, board):
        self._board = Board(board)

    def solve(self):
        row_index = 0
        col_index = 0
        while row_index < 3:
            if col_index == 9:
                row_index += 1
                col_index = 0

            numbers = [str(num) for num in range(1, 10)]
            if self._board.get_value(row_index, col_index) == '.':
                for number in numbers:
                    if self._test_row(row_index, number) and self._test_col(col_index, number) and \
                            self._test_square(row_index, col_index, number):
                        self._board.update_board(row_index, col_index, number)
                        col_index += 1
                        break
                else:
                    row_index, col_index = self._back_propagate(row_index, col_index - 1)
            elif not self._board.get_board_presets()[row_index][col_index]:
                start_num = self._board.get_value(row_index, col_index)
                numbers = [str(num) for num in range(int(start_num), 10)]
                for number in numbers:
                    if self._test_row(row_index, number) and self._test_col(col_index, number) and \
                            self._test_square(row_index, col_index, number):
                        self._board.update_board(row_index, col_index, number)
                        col_index += 1
                        break
                else:
                    self._board.update_board(row_index, col_index, '.')
                    row_index, col_index = self._back_propagate(row_index, col_index - 1)
            else:
                col_index += 1
            print(row_index, col_index)
            self._print_board()
            print()

    def _back_propagate(self, row_index, col_index):
        if col_index == -1:
            row_index -= 1
            col_index = 8

        if self._board.get_board()[row_index][col_index] != '9' and not \
                self._board.get_board_presets()[row_index][col_index]:
            return row_index, col_index
        elif self._board.get_board()[row_index][col_index] == '9' and not \
                self._board.get_board_presets()[row_index][col_index]:
            self._board.update_board(row_index, col_index, '.')
            return self._back_propagate(row_index, col_index - 1)
        elif self._board.get_board_presets()[row_index][col_index]:
            return self._back_propagate(row_index, col_index - 1)

    def _test_row(self, row_index: int, number: str) -> bool:
        if number not in self._board.get_board()[row_index]:
            return True
        return False

    def _test_col(self, col_index: int, number: str):
        for row in self._board.get_board():
            if number not in row[col_index]:
                continue
            else:
                return False
        return True

    def _test_square(self, row_index: int, col_index: int, number: str):
        quadrants = {1: (self._board.get_board()[0][0:3] + self._board.get_board()[1][0:3] +
                         self._board.get_board()[2][0:3]),
                     2: (self._board.get_board()[0][3:6] + self._board.get_board()[1][3:6] +
                         self._board.get_board()[2][3:6]),
                     3: (self._board.get_board()[0][6:] + self._board.get_board()[1][6:] +
                         self._board.get_board()[2][6:])}

        if row_index == 0 and col_index < 3:
            if number not in quadrants[1]:
                return True
            return False
        elif row_index == 0 and col_index < 6:
            if number not in quadrants[2]:
                return True
            return False
        elif row_index == 0 and col_index >= 6:
            if number not in quadrants[3]:
                return True
            return False
        elif row_index == 1 and col_index < 3:
            if number not in quadrants[1]:
                return True
            return False
        elif row_index == 1 and col_index < 6:
            if number not in quadrants[2]:
                return True
            return False
        elif row_index == 1 and col_index >= 6:
            if number not in quadrants[3]:
                return True
            return False
        elif row_index == 2 and col_index < 3:
            if number not in quadrants[1]:
                return True
            return False
        elif row_index == 2 and col_index < 6:
            if number not in quadrants[2]:
                return True
            return False
        elif row_index == 2 and col_index >= 6:
            if number not in quadrants[3]:
                return True
            return False

    def _print_board(self):
        for row in self._board.get_board():
            print(row)


class Board(object):
    """Represents a board used to play Sudoku with."""
    def __init__(self, board):
        self._board = board
        self._board_presets = self._find_presets()

    def get_board(self):
        """Returns the current state of the Sudoku board."""
        return self._board

    def get_board_presets(self):
        """Returns the boolean representation of the original Sudoku board where True represents a preset value and
        False represents a blank space on the board."""
        return self._board_presets

    def get_value(self, row_index, col_index):
        return self._board[row_index][col_index]

    def update_board(self, row_index: int, col_index: int, number: str):
        self._board[row_index][col_index] = number

    def _find_presets(self):
        """Returns a boolean representation of the original Sudoku board where True represents a preset value and False
        represents a blank space on the board."""
        board_presets = []
        for row_index, row in enumerate(self._board):
            row_presets = []
            for col_index, value in enumerate(row):
                if value == '.':
                    row_presets.append(False)
                else:
                    row_presets.append(True)
            board_presets.append(row_presets)
        return board_presets


if __name__ == "__main__":
    sudoku_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    solve = SolveSudoku(sudoku_board)
    solve.solve()
