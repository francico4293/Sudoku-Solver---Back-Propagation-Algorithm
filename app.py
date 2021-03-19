import sys

from button import *


class App(object):
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sudoku Solver")
        self.solve = False
        self.running = True
        self.building = True
        self.mouse_pos = None
        self.grid = None
        self.selected = None
        self.selected_x = None
        self.selected_y = None
        self.solve_selected = None
        self.row_dict = None
        self.col_dict = None
        self.sub_box_dict = None
        self.sudoku_board = None
        self.board = board
        self.font = pygame.font.SysFont("ariel", 40)
        self.buttons = []
        self.load_buttons()

# Main Methods:

    def run(self):
        while self.running:
            self.update_build()
            if self.building:
                self.draw_build()
            pygame.display.update()
        pygame.quit()
        sys.exit()

    def update_build(self):
        for button in self.buttons:
            button.update(pygame.mouse.get_pos())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_pos = pygame.mouse.get_pos()
                if self.mouse_on_board(self.mouse_pos):
                    self.selected = self.find_location()
                else:
                    self.selected = None
                for button in self.buttons:
                    if button.click():
                        self.building = False
                        self.solve = True
                        self.create_dicts()
                        self.solve_sudoku()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_1 or event.key == pygame.K_KP1) and self.selected:
                    board[self.selected[1] - 1][self.selected[0] - 1] = '1'
                if (event.key == pygame.K_2 or event.key == pygame.K_KP2) and self.selected:
                    board[self.selected[1] - 1][self.selected[0] - 1] = '2'
                if (event.key == pygame.K_3 or event.key == pygame.K_KP3) and self.selected:
                    board[self.selected[1] - 1][self.selected[0] - 1] = '3'
                if (event.key == pygame.K_4 or event.key == pygame.K_KP4) and self.selected:
                    board[self.selected[1] - 1][self.selected[0] - 1] = '4'
                if (event.key == pygame.K_5 or event.key == pygame.K_KP5) and self.selected:
                    board[self.selected[1] - 1][self.selected[0] - 1] = '5'
                if (event.key == pygame.K_6 or event.key == pygame.K_KP6) and self.selected:
                    board[self.selected[1] - 1][self.selected[0] - 1] = '6'
                if (event.key == pygame.K_7 or event.key == pygame.K_KP7) and self.selected:
                    board[self.selected[1] - 1][self.selected[0] - 1] = '7'
                if (event.key == pygame.K_8 or event.key == pygame.K_KP8) and self.selected:
                    board[self.selected[1] - 1][self.selected[0] - 1] = '8'
                if (event.key == pygame.K_9 or event.key == pygame.K_KP9) and self.selected:
                    board[self.selected[1] - 1][self.selected[0] - 1] = '9'
                if (event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE) and self.selected:
                    board[self.selected[1] - 1][self.selected[0] - 1] = '.'

    def update_solve(self):
        self.text_to_board()

    def draw_build(self):
        self.window.fill(WHITE)

        for button in self.buttons:
            button.draw(self.window)

        if self.selected:
            self.shade_cell()

        self.draw_grid()
        self.text_to_board()

    def draw_update(self):
        self.window.fill(WHITE)

        for button in self.buttons:
            button.draw(self.window)

        if self.solve_selected:
            self.shade_cell_solve()

        self.draw_grid()
        self.text_to_board()

# Helper Methods:

    def draw_grid(self):
        # Board frame:
        self.grid = pygame.draw.rect(self.window, BLACK, (GRID_POS[0], GRID_POS[1],
                                                          WIDTH - 150, HEIGHT - 150), 2)

        # Grid lines:
        for x in range(1, 10):
            if x % 3 == 0:
                pygame.draw.line(self.window, BLACK, ((x * CELL_SIZE) + GRID_POS[0], GRID_POS[1]),
                                 ((x * CELL_SIZE) + GRID_POS[0], HEIGHT - 50), 2)
                pygame.draw.line(self.window, BLACK, (GRID_POS[0], (x * CELL_SIZE) + GRID_POS[1]),
                                 (WIDTH - 75, (x * CELL_SIZE) + GRID_POS[1]), 2)
            else:
                pygame.draw.line(self.window, BLACK, ((x * CELL_SIZE) + GRID_POS[0], GRID_POS[1]),
                                 ((x * CELL_SIZE) + GRID_POS[0], HEIGHT - 50))
                pygame.draw.line(self.window, BLACK, (GRID_POS[0], (x * CELL_SIZE) + GRID_POS[1]),
                                 (WIDTH - 75, (x * CELL_SIZE) + GRID_POS[1]))

    def mouse_on_board(self, mouse):
        if (self.grid[2] + GRID_POS[0] > mouse[0] > self.grid[0]) and \
                (self.grid[3] + GRID_POS[1] > mouse[1] > self.grid[1]):
            return True
        else:
            return False

    def find_location(self):
        adj_x = self.mouse_pos[0] - GRID_POS[0]
        adj_y = self.mouse_pos[1] - GRID_POS[1]

        grid_x = None
        grid_y = None
        for key in grid_cell.keys():
            if grid_cell[key][1] > adj_x > grid_cell[key][0]:
                grid_x = key
                self.selected_x = grid_cell[key][0]
            if grid_cell[key][1] > adj_y > grid_cell[key][0]:
                grid_y = key
                self.selected_y = grid_cell[key][0]

        return grid_x, grid_y

    def shade_cell(self):
        pygame.draw.rect(self.window, BLUE, (self.selected_x + GRID_POS[0],
                                             self.selected_y + GRID_POS[1], CELL_SIZE, CELL_SIZE))

    def shade_cell_solve(self):
        pygame.draw.rect(self.window, RED, (self.solve_selected[1] * CELL_SIZE + GRID_POS[0],
                                            self.solve_selected[0] * CELL_SIZE + GRID_POS[1], CELL_SIZE, CELL_SIZE))

    def text_to_board(self):
        row_num = -1
        for row in self.board:
            row_num += 1
            col_num = -1
            for value in row:
                col_num += 1
                if value != '.':
                    number = self.font.render(value, False, BLACK)
                    self.window.blit(number, (((CELL_SIZE - number.get_size()[0]) // 2) +
                                              GRID_POS[0] + CELL_SIZE * col_num,
                                              ((CELL_SIZE - number.get_size()[1]) // 2) +
                                              GRID_POS[1] + CELL_SIZE * row_num))

    def load_buttons(self):
        self.buttons.append(Button(40, 40, 125, 40, text='Solve Puzzle'))

# Back propagation algorithm:
    def solve_sudoku(self):
        row = 1  # initial row
        col = 0  # initial column
        while '.' in (self.row_dict[1] and self.row_dict[2] and self.row_dict[3] and
                      self.row_dict[4] and self.row_dict[5] and self.row_dict[6] and
                      self.row_dict[7] and self.row_dict[8] and self.row_dict[9]):
            row, col = self.update_value(row, col)
            self.solve_selected = (row - 1, col - 1)
            value_to_update = self.board[row - 1][col - 1]
            self.board[row - 1][col - 1] = '.'
            self.draw_update()
            pygame.display.update()
            self.board[row - 1][col - 1] = value_to_update
            self.text_to_board()
            pygame.display.update()
            if col == 9:
                row += 1
                col = 0
        pygame.display.update()

    def update_value(self, row, column):
        board_info = self.sudoku_board[row][column]
        if board_info[0] == '.':  # board space is empty
            temp_row, temp_col = self.find_num(row, column, board_info)
            if temp_row and temp_col:
                column = temp_col
                return row, column
            else:
                return self.back_prop(row, column)
        else:  # board space is pre-filled
            column += 1
            return row, column

    def back_prop(self, row, column):
        column -= 1
        if column < 0:
            row -= 1
            column = 9
            return self.back_prop(row, column)
        board_info = self.sudoku_board[row][column]
        while len(board_info) == 4:
            column -= 1
            if column < 0:
                break
            board_info = self.sudoku_board[row][column]
        if column < 0:
            row -= 1
            column = 9
            return self.back_prop(row, column)
        if board_info[0] == '9':
            self.find_num(row, column, board_info, bp=True)
            return self.back_prop(row, column)
        else:
            number = str(int(board_info[0]) + 1)
            while self.find_num(row, column, board_info, bp=True, number=number):
                number = int(number) + 1
                if number == 10:
                    self.find_num(row, column, board_info, bp=True)
                    return self.back_prop(row, column)
                number = str(number)
            return row, column + 1

    def find_num(self, row, column, board_info, bp=False, number=None):
        if bp and not number:
            board_info[0] = '.'
            self.row_dict[row][column] = '.'
            self.col_dict[board_info[1]][row - 1] = '.'
            self.sub_box_dict[board_info[2]][self.update_sub_box_dict(row, board_info[1], board_info[2])] = '.'
        elif bp and number:
            if number not in self.row_dict[row] and number not in self.col_dict[board_info[1]] \
                    and number not in self.sub_box_dict[board_info[2]]:
                board_info[0] = number
                self.row_dict[row][column] = number
                self.col_dict[board_info[1]][row - 1] = number
                self.sub_box_dict[board_info[2]][self.update_sub_box_dict(row, board_info[1],
                                                                          board_info[2])] = number
                return False
            return True
        else:
            numbers = '123456789'
            for number in numbers:
                if number not in self.row_dict[row] and number not in self.col_dict[board_info[1]] \
                        and number not in self.sub_box_dict[board_info[2]]:
                    board_info[0] = number
                    self.row_dict[row][column] = number
                    self.col_dict[board_info[1]][row - 1] = number
                    self.sub_box_dict[board_info[2]][self.update_sub_box_dict(row, board_info[1],
                                                                              board_info[2])] = number
                    column += 1
                    return row, column

            return None, None

    @staticmethod
    def update_sub_box_dict(row, column, sub_box):
        conversion_dict = {1: {1: [[1, 1], [2, 2], [3, 3]],
                               2: [[1, 4], [2, 5], [3, 6]],
                               3: [[1, 7], [2, 8], [3, 9]]},
                           2: {1: [[4, 1], [5, 2], [6, 3]],
                               2: [[4, 4], [5, 5], [6, 6]],
                               3: [[4, 7], [5, 8], [6, 9]]},
                           3: {1: [[7, 1], [8, 2], [9, 3]],
                               2: [[7, 4], [8, 5], [9, 6]],
                               3: [[7, 7], [8, 8], [9, 9]]},
                           4: {4: [[1, 1], [2, 2], [3, 3]],
                               5: [[1, 4], [2, 5], [3, 6]],
                               6: [[1, 7], [2, 8], [3, 9]]},
                           5: {4: [[4, 1], [5, 2], [6, 3]],
                               5: [[4, 4], [5, 5], [6, 6]],
                               6: [[4, 7], [5, 8], [6, 9]]},
                           6: {4: [[7, 1], [8, 2], [9, 3]],
                               5: [[7, 4], [8, 5], [9, 6]],
                               6: [[7, 7], [8, 8], [9, 9]]},
                           7: {7: [[1, 1], [2, 2], [3, 3]],
                               8: [[1, 4], [2, 5], [3, 6]],
                               9: [[1, 7], [2, 8], [3, 9]]},
                           8: {7: [[4, 1], [5, 2], [6, 3]],
                               8: [[4, 4], [5, 5], [6, 6]],
                               9: [[4, 7], [5, 8], [6, 9]]},
                           9: {7: [[7, 1], [8, 2], [9, 3]],
                               8: [[7, 4], [8, 5], [9, 6]],
                               9: [[7, 7], [8, 8], [9, 9]]}}

        for key in conversion_dict[sub_box]:
            if row == key:
                for conversion in conversion_dict[sub_box][key]:
                    if column == conversion[0]:
                        return conversion[1] - 1

    def create_dicts(self):
        # create row dictionary
        row_count = 0
        row_dictionary = self.dict_struct()
        for row in board:
            row_count += 1
            row_dictionary[row_count] = row

        # create column dictionary
        column_dictionary = self.dict_struct()
        for row in board:
            for index in range(0, len(row)):
                column_dictionary[index + 1].append(row[index])

        # create sub-box dictionary
        row_count = 0
        sub_box_dictionary = self.dict_struct()
        for row in board:
            row_count += 1
            for index in range(0, len(row)):
                sub_box_dictionary[self.sub_box_key(row_count, index)].append(row[index])

        # create board dictionary
        row_count = 0
        board_dictionary = self.dict_struct()
        for row in board:
            row_count += 1
            for index, number in enumerate(row):
                if number == '.':
                    board_dictionary[row_count].append([row[index], index + 1,
                                                        self.sub_box_key(row_count, index)])
                else:
                    board_dictionary[row_count].append([row[index], index + 1, self.sub_box_key(row_count, index), 'p'])

        self.row_dict = row_dictionary
        self.col_dict = column_dictionary
        self.sub_box_dict = sub_box_dictionary
        self.sudoku_board = board_dictionary

    @staticmethod
    def dict_struct():
        dictionary = {1: [],
                      2: [],
                      3: [],
                      4: [],
                      5: [],
                      6: [],
                      7: [],
                      8: [],
                      9: []}

        return dictionary

    @staticmethod
    def sub_box_key(row_count, index):
        if 3 >= row_count >= 1:
            if 3 >= index + 1 >= 1:
                return 1
            elif 6 >= index + 1 >= 4:
                return 2
            else:
                return 3
        elif 6 >= row_count >= 4:
            if 3 >= index + 1 >= 1:
                return 4
            elif 6 >= index + 1 >= 4:
                return 5
            else:
                return 6
        else:  # rows 7-9
            if 3 >= index + 1 >= 1:
                return 7
            elif 6 >= index + 1 >= 4:
                return 8
            else:
                return 9
