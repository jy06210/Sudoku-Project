import pygame
from Constants import *
from sudoku_generator import SudokuGenerator


class Board(SudokuGenerator):
    def __init__(self, width, height, screen, difficulty,row_length, removed_cells, board):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected_row = 0
        self.selected_col = 0
        self.board=board
        SudokuGenerator.__init__(self, row_length, removed_cells)
    '''Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
       Draws every cell on this board.
   '''
    def draw(self):
        value_font = pygame.font.Font(None, FONT)
        #draw row
        for i in range (0,10):
            if i%3!=0:
                pygame.draw.line(self.screen, (0,0,0),(0,i*70), (630, i*70))
            else:
                pygame.draw.line(self.screen, (0,0,0), (0, i*70), (630, i*70), (1))
        #draw col
        for i in range (0,10):
            if i%3!=0:
                pygame.draw.line(self.screen, (0,0,0), (i*70, 0), (i*70,630))
            else:
                pygame.draw.line(self.screen, (0,0,0), (0, i*70), (630, i*70), 1)
        #draw numbers in cells
        for i in range(0,9):
            for j in range(0,9):
                sketched_value = self.sketch(self.board[i][j])
                cell_surf=value_font.render(sketched_value,0,(0,0,0))
                cell_rect=cell_surf.get_rect(topleft=(SCREEN_SIZE // 9 * i, SCREEN_SIZE // 9 * j))
                self.screen.blit(cell_surf,cell_rect)

    '''Marks the cell at (row, col) in the board as the current selected cell.
	Once a cell has been selected, the user can edit its value or sketched value.
    '''
    def select(self, row, col):
        self.selected_row = row
        self.selected_col = col

    '''If a tuple of (x,y) coordinates is within the displayed board, 
    this function returns a tuple of the (row, col) of the cell which was clicked. 
    Otherwise, this function returns None.
    '''
    def click(self, prow, pcol):
        if prow <= 630 and pcol <= 630:
            row = prow//70
            col = pcol//70
            return row, col
        return None

    '''Clears the value cell. 
    Note that the user can only remove the cell values and 
    sketched values that are filled by themselves.
    '''
    def clear(self):
        if (self.selected_row, self.selected_col) in self.removed_cells_list:
            self.board[self.selected_row][self.selected_col] = 0

    '''Sets the sketched value of the current selected cell equal to the user entered value.
	It will be displayed at the top left corner of the cell using the draw() function.
    '''
    def sketch(self, value):
        if value == 0:
            return ""
        else:
            return value

    '''Sets the value of the current selected cell equal to the user entered value. 
    Called when the user presses the Enter key.
    '''
    def place_number(self, value):
        self.board[self.selected_row][self.selected_col] = value


    '''Resets all cells in the board to their original values 
    (0 if cleared, otherwise the corresponding digit).
    '''
    def reset_to_original(self):
        for row in range(1, 10):
            for col in range(1, 10):
                if (row, col) in self.removed_cells_list:
                    self.board[row][col] = 0
                else:
                    self.board[row][col] = self.board[row][col]


    '''Returns a Boolean value indicating whether the board is full or not.'''
    def is_full(self):
        if 0 in self.board:
            return False
        else:
            return True

    '''Updates the underlying 2D board with the values in all cells.'''
    def update_board(self):
        pass

    '''Finds an empty cell and returns its row and col as a tuple (x,y).
    '''
    def find_empty(self):
        for row in range(1, 10):
            for col in range(1, 10):
                if self.board[row][col] == 0:
                    return row, col


    '''Check whether the Sudoku board is solved correctly.'''
    '''
    def check_board(self):
        for row in range(1, 10):
            for col in range(1, 10):
                if self.board[row][col] == self.fill_values():
    '''


