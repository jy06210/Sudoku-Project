import pygame
import sudoku_generator
from sudoku_generator import SudokuGenerator


class Board(SudokuGenerator):
    def __init__(self, width, height, screen, difficulty,row_length, removed_cells):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        SudokuGenerator.__init__(self, row_length, removed_cells)
    '''Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
       Draws every cell on this board.
   '''
    def draw(self):
        #draw row
        for i in range (0,10):
            if i%3!=0:
                pygame.draw.line(self.screen, (0,0,0),(0,i*100), (900, i*100))
            else:
                pygame.draw.line(self.screen, (0,0,0), (0, i*100), (900, i*100), (10))
        #draw col
        for i in range (0,10):
            if i%3!=0:
                pygame.draw.line(self.screen, (0,0,0), (i*100, 0), (i*100,900))
            else:
                pygame.draw.line(self.screen, (0,0,0), (0, i*100), (900, i*100))


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
        if prow <= 900 and pcol <= 900:
            row = prow//100
            col = pcol//100
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
        pass

    '''Sets the value of the current selected cell equal to the user entered value. 
    Called when the user presses the Enter key.
    '''
    def place_number(self, value):
        self.board[self.selected_row][self.selected_col] = value

    '''Resets all cells in the board to their original values 
    (0 if cleared, otherwise the corresponding digit).
    '''
    def reset_to_original(self):
        for row in range(9):
            for col in range(9):
                if (row, col) in self.removed_cells_list:
                    self.grid[row][col] = 0
                else:
                    self.grid[row][col] = self.original_board[row][col]


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
        pass

    '''Check whether the Sudoku board is solved correctly.'''
    def check_board(self):
        pass

