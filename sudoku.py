import pygame, sys
from sudoku_generator import *
from board import *
from cell import *
from Constants import *



pygame.init()
game_over=False
screen=pygame.display.set_mode((630, 700))
pygame.display.set_caption("Sudoku")
screen.fill((255,255,255))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    sudoku_board = generate_sudoku(9, 30)
    board = Board(630, 630, screen, 1, 9, 30, sudoku_board)
    board.draw()
    pygame.display.flip()



