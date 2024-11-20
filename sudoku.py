import pygame, sys
from sudoku_generator import *
from board import *
from cell import *
from Constants import *

pygame.init()
game_over=False
screen=pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sudoku")
screen.fill((0,0,0))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

