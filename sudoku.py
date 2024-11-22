import pygame, sys
from pygame import MOUSEBUTTONDOWN

from sudoku_generator import *
from board import *
from cell import *
from Constants import *



pygame.init()
game_over=False
screen=pygame.display.set_mode((630, 700))
pygame.display.set_caption("Sudoku")
screen.fill((255,255,255))
sudoku_board = generate_sudoku(9, 30)
board = Board(630, 630, screen, 1, 9, 30, sudoku_board)
board.draw()
pygame.display.flip()
clicked=False
while True:
    board.draw()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==MOUSEBUTTONDOWN:
            x,y= event.pos
            row, col= board.click(x,y)
            print(row, col)
            clicked=True
        if event.type==pygame.KEYDOWN and clicked:
            print("Down")
            if event.key==pygame.K_1:
                print("Key 1 pressed")
                board.update_board(1, row, col)
                print(board.board)
            if event.key==pygame.K_2:
                board.update_board(2, row, col)
            if event.key==pygame.K_3:
                board.update_board(3, row, col)
            if event.key==pygame.K_4:
                board.update_board(4, row, col)
            if event.key==pygame.K_5:
                board.update_board(5, row, col)
            if event.key==pygame.K_6:
                board.update_board(6, row, col)







