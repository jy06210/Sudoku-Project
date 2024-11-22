import pygame, sys
from pygame import MOUSEBUTTONDOWN

from sudoku_generator import *
from board import *
from cell import *
from Constants import *



pygame.init()
game_over = False
screen=pygame.display.set_mode((630, 700))
pygame.display.set_caption("Sudoku")
screen.fill((255,255,255))
sudoku_board, correct_board = generate_sudoku(9, 5)
answer=correct_board
board = Board(630, 630, screen, 1, 9, 30, sudoku_board)
board.draw()
pygame.display.flip()
clicked = False
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and not game_over:
            x,y = event.pos
            row, col = board.click(x,y)
            clicked = True
        if event.type==pygame.KEYDOWN and clicked:
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
            if board.is_full():
                game_over = True


    if game_over:
        board.draw_cell()
        pygame.display.flip()
        pygame.time.delay(1000)
        if board.board==answer:
            correct=True
        board.reset_to_original()
        screen.fill((255, 255, 255))
        if correct:
            value_font = pygame.font.Font(None, FONT)
            sketched_value="You Won!"
            cell_surf = value_font.render(sketched_value, 0, (0, 0, 0))
            cell_rect = cell_surf.get_rect(center=(315, 315))
            screen.blit(cell_surf, cell_rect)

        else:
            value_font = pygame.font.Font(None, FONT)
            sketched_value = "You lose!"
            cell_surf = value_font.render(sketched_value, 0, (0, 0, 0))
            cell_rect = cell_surf.get_rect(center=(315, 315))
            screen.blit(cell_surf, cell_rect)


        pygame.display.flip()

    else:
        screen.fill((255,255,255))
        board.draw()
        board.draw_cell()
        if clicked:
            board.select(row,col)
        pygame.display.flip()






