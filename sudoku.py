import pygame, sys
from sudoku_generator import *
from board import *
from cell import *

def draw_start_screen():
    screen.fill((255,192,203))
pygame.init()
game_over=False
screen=pygame.display.set_mode((900, 1000))
screen.fill((255,192,203))
board=Board(900,900,screen,1,9,30)
board.generate_sudoku()
board.draw()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN and not game_over:
            x,y=event.pos
            row, col= board.click(x,y)
            
