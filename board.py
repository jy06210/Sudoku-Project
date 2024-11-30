import pygame
from Constants import *
import copy



class Board:
    def __init__(self, width, height, screen, difficulty, row_length, removed_cells, board):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected_row = 0
        self.selected_col = 0
        self.board = board
        self.original_board = copy.deepcopy(board)
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
                pygame.draw.line(self.screen, (0,0,0), (0, i*70), (630, i*70), 5)
        #draw col
        for i in range (0,10):
            if i%3!=0:
                pygame.draw.line(self.screen, (0,0,0), (i*70, 0), (i*70,630))
            else:
                pygame.draw.line(self.screen, (0,0,0), (i*70,0), (i*70,630), 5)
        for i in range(0, 9):
            for j in range(0, 9):
                sketched_value = self.sketch(self.original_board[i][j])
                cell_surf = value_font.render(sketched_value, 0, (0, 0, 0))
                cell_rect = cell_surf.get_rect(center=(i * 70 + 35, j * 70 + 35))
                self.screen.blit(cell_surf, cell_rect)

    def draw_cell(self):
        value_font = pygame.font.Font(None, FONT)
        for i in range(0,9):
            for j in range(0,9):
                if self.original_board[i][j]==0:
                    sketched_value=self.sketch(self.board[i][j])
                    cell_surf=value_font.render(sketched_value,0,(255,0,0))
                    cell_rect=cell_surf.get_rect(center=(i * 70 + 35, j * 70 + 35))
                    self.screen.blit(cell_surf,cell_rect)

    '''Marks the cell at (row, col) in the board as the current selected cell.
	Once a cell has been selected, the user can edit its value or sketched value.
    '''
    def select(self, row, col):
        i=row-1
        j=col-1
        pygame.draw.line(self.screen, (255,0,0), (i*70,j*70),(i*70+70,j*70),5)
        pygame.draw.line(self.screen, (255,0,0), (i*70,j*70+70),(i*70+70,j*70+70),5)
        pygame.draw.line(self.screen, (255,0,0), (i*70,j*70),(i*70,j*70+70),5)
        pygame.draw.line(self.screen, (255,0,0), (i*70+70, j*70),(i*70+70,j*70+70),5)

    '''If a tuple of (x,y) coordinates is within the displayed board, 
    this function returns a tuple of the (row, col) of the cell which was clicked. 
    Otherwise, this function returns None.
    '''
    # def click(self, prow, pcol):
    #     if prow <= 630 and pcol <= 630:
    #         row = prow//70 + 1
    #         col = pcol//70 + 1
    #         return row, col
    #     return None
    def click(self, prow, pcol):
        """Determine the row and column based on the click position."""
        if 0 <= prow < 630 and 0 <= pcol < 630:  # Ensure click is within bounds
            row = prow // 70 +1 # Integer division to get the row
            col = pcol // 70 +1# Integer division to get the column
            return row, col
        return None  # Return None if the click is out of bounds

    '''Clears the value cell. 
    Note that the user can only remove the cell values and 
    sketched values that are filled by themselves.
    '''
    def clear(self, row, col):
        if self.original_board[row-1][col-1] == 0:
            self.board[row-1][col-1] = 0

    '''Sets the sketched value of the current selected cell equal to the user entered value.
	It will be displayed at the top left corner of the cell using the draw() function.
    '''
    def sketch(self, value):
        if value == 0:
            return ""
        else:
            return str(value)

    '''Sets the value of the current selected cell equal to the user entered value. 
    Called when the user presses the Enter key.
    '''
    def place_number(self, value):
        self.board[self.selected_row][self.selected_col] = value


    '''Resets all cells in the board to their original values 
    (0 if cleared, otherwise the corresponding digit).
    '''
    def reset_to_original(self):
        self.board=copy.deepcopy(self.original_board)


    '''Returns a Boolean value indicating whether the board is full or not.'''
    def is_full(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return False
        return True

    '''Updates the underlying 2D board with the values in all cells.'''
    def update_board(self,number, row, col):
        if self.original_board[row-1][col-1]== 0:
            self.board[row-1][col-1] = number


    '''Finds an empty cell and returns its row and col as a tuple (x,y).
    '''
    def find_empty(self):
        for row in range(1, 10):
            for col in range(1, 10):
                if self.board[row][col] == 0:
                    return row, col


    def valid_in_row(self, row, num):
        count=0
        row=int(row)
        for r in self.board:
            if num in r:
                count+=1
        if count!=1:
            return False
        else:
            return True

    def valid_in_col(self, col, num):
        count = 0
        col=int(col)
        for i in range(0, 9):
            if num == self.board[i][col]:
                count+=1
        if count!=1:
            return False
        else:
            return True


    def valid_in_box(self, row_start, col_start, num):
        count=0
        for i in range(row_start, row_start+3):
            for j in range(col_start, col_start+3):
                if num == self.board[i][j]:
                    count+=1
        if count!=1:
            return False
        return True

    def is_valid(self, row, col, num):
        row_start=row//3 * 3
        col_start=col//3 * 3
        if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row_start, col_start, num):
            return True
        return False

    '''Check whether the Sudoku board is solved correctly.'''
    def check_board(self, answer):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] != answer[row][col]:
                    return False
        return True


