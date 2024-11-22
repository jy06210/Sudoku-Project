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
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==MOUSEBUTTONDOWN:
            x,y= event.pos
            row, col= board.click(x,y)
            clicked=True
        if event.type==pygame.KEYDOWN and clicked:
            print("Down")
            if event.key==pygame.K_1:
                board.update_board(1, row, col)
                clicked=False
            if event.key==pygame.K_2:
                board.update_board(2, row, col)
                clicked=False
            if event.key==pygame.K_3:
                board.update_board(3, row, col)
                clicked=False
            if event.key==pygame.K_4:
                board.update_board(4, row, col)
                clicked=False
            if event.key==pygame.K_5:
                board.update_board(5, row, col)
                clicked=False
            if event.key==pygame.K_6:
                board.update_board(6, row, col)
                clicked=False
            if event.key==pygame.K_7:
                board.update_board(7, row, col)
                clicked=False
            if event.key==pygame.K_8:
                board.update_board(8, row, col)
                clicked=False
            if event.key==pygame.K_9:
                board.update_board(9, row, col)
                clicked=False
            if event.key==pygame.K_BACKSPACE:
                board.clear(row, col)
                clicked = False
    screen.fill((255,255,255))
    board.draw()
    board.draw_cell()
    if clicked==True:
        board.select(row,col)
    pygame.display.flip()







