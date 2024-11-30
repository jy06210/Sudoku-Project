# # import pygame, sys
# # from pygame import MOUSEBUTTONDOWN
# # from BUTT import create_reset_button, draw_reset_button
# # from sudoku_generator import *
# # from board import *
# # from cell import *
# # from Constants import *
# #
# #
# #
# # pygame.init()
# #
# # game_over = False
# # screen=pygame.display.set_mode((630, 700))
# # pygame.display.set_caption("Sudoku")
# #
# # #screen.fill((255,255,255))
# #
# # sudoku_board, correct_board = generate_sudoku(9, 3)
# # answer=correct_board
# # board = Board(630, 630, screen, 1, 9, 30, sudoku_board)
# # butt1_surface, butt_rect1 = create_reset_button()
# # #board.draw()
# # #pygame.display.flip()
# # clicked = False
# #
# #
# #
# # while True:
# #     #draw_reset_button(screen, butt1_surface, butt_rect1)
# #     for event in pygame.event.get():
# #         if event.type == pygame.MOUSEBUTTONDOWN:
# #             if butt_rect1.collidepoint(event.pos):
# #                 board.reset_to_original()
# #         if event.type==pygame.QUIT:
# #             sys.exit()
# #         if event.type == MOUSEBUTTONDOWN and not game_over:
# #             x,y = event.pos
# #             row, col = board.click(x,y)
# #             clicked = True
# #         if event.type==pygame.KEYDOWN and clicked:
# #             if event.key==pygame.K_1:
# #                 board.update_board(1, row, col)
# #                 clicked=False
# #             if event.key==pygame.K_2:
# #                 board.update_board(2, row, col)
# #                 clicked=False
# #             if event.key==pygame.K_3:
# #                 board.update_board(3, row, col)
# #                 clicked=False
# #             if event.key==pygame.K_4:
# #                 board.update_board(4, row, col)
# #                 clicked=False
# #             if event.key==pygame.K_5:
# #                 board.update_board(5, row, col)
# #                 clicked=False
# #             if event.key==pygame.K_6:
# #                 board.update_board(6, row, col)
# #                 clicked=False
# #             if event.key==pygame.K_7:
# #                 board.update_board(7, row, col)
# #                 clicked=False
# #             if event.key==pygame.K_8:
# #                 board.update_board(8, row, col)
# #                 clicked=False
# #             if event.key==pygame.K_9:
# #                 board.update_board(9, row, col)
# #                 clicked=False
# #             if event.key==pygame.K_BACKSPACE:
# #                 board.clear(row, col)
# #                 clicked = False
# #             if board.is_full():
# #                 game_over = True
# #
# #
# #     if game_over:
# #         board.draw_cell()
# #         pygame.display.flip()
# #         pygame.time.delay(1000)
# #         if board.is_full():
# #             correct = board.check_board(answer)
# #         board.reset_to_original()
# #         screen.fill((255, 255, 255))
# #         sketched_value = "You Won!" if correct else "You lose!"
# #         value_font = pygame.font.Font(None, FONT)
# #         cell_surf = value_font.render(sketched_value, 0, (0, 0, 0))
# #         cell_rect = cell_surf.get_rect(center=(315, 315))
# #         screen.blit(cell_surf, cell_rect)
# #         pygame.display.flip()
# #
# #     else:
# #         screen.fill((255,255,255))
# #         board.draw()
# #         board.draw_cell()
# #         if clicked:
# #             board.select(row,col)
# #         pygame.display.flip()
# #
# #
# #
import pygame, sys
from pygame import MOUSEBUTTONDOWN
from BUTT import create_reset_button, draw_reset_button, create_restart_button, draw_restart_button, draw_exit_button, create_exit_button
from sudoku_generator import *
from board import *
from cell import *
from Constants import *

# Initialize Pygame
pygame.init()

# Game variables
game_over = False
screen = pygame.display.set_mode((630, 700))
pygame.display.set_caption("Sudoku")

# Create Sudoku board and reset button
sudoku_board, correct_board = generate_sudoku(9, 6)
answer = correct_board
board = Board(630, 630, screen, 1, 9, 30, sudoku_board)
butt1_surface, butt_rect1 = create_reset_button() # Create reset button
butt2_surface, butt_rect2 = create_restart_button()
butt3_surface, butt_rect3 = create_exit_button()

clicked = False
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            # Handle reset button click
            if butt_rect1.collidepoint(event.pos):
                board.reset_to_original()
                clicked = False
            # Handle restart button click
            elif butt_rect2.collidepoint(event.pos):
                # Logic for restarting the game
                sudoku_board, correct_board = generate_sudoku(9, 6)
                answer = correct_board
                board = Board(630, 630, screen, 1, 9, 30, sudoku_board)
                clicked = False
            # Handle board cell clicks
            elif butt_rect3.collidepoint(event.pos):
                sys.exit()
            elif not game_over:
                x, y = event.pos
                result = board.click(x, y)  # Call the click method
                if result is not None:
                    row, col = result
                    clicked = True

        if event.type == pygame.KEYDOWN and clicked:
            if event.key == pygame.K_1:
                board.update_board(1, row, col)
                clicked = False
            elif event.key == pygame.K_2:
                board.update_board(2, row, col)
                clicked = False
            elif event.key == pygame.K_3:
                board.update_board(3, row, col)
                clicked = False
            elif event.key == pygame.K_4:
                board.update_board(4, row, col)
                clicked = False
            elif event.key == pygame.K_5:
                board.update_board(5, row, col)
                clicked = False
            elif event.key == pygame.K_6:
                board.update_board(6, row, col)
                clicked = False
            elif event.key == pygame.K_7:
                board.update_board(7, row, col)
                clicked = False
            elif event.key == pygame.K_8:
                board.update_board(8, row, col)
                clicked = False
            elif event.key == pygame.K_9:
                board.update_board(9, row, col)
                clicked = False
            elif event.key == pygame.K_BACKSPACE:
                board.clear(row, col)
                clicked = False
            if board.is_full():
                game_over = True

    # Game over logic
    if game_over:
        board.draw_cell()
        pygame.display.flip()
        pygame.time.delay(1000)
        if board.is_full():
            correct = board.check_board(answer)
        board.reset_to_original()
        screen.fill((255, 255, 255))
        sketched_value = "You Won!" if correct else "You Lose!"
        value_font = pygame.font.Font(None, FONT)
        cell_surf = value_font.render(sketched_value, 0, (0, 0, 0))
        cell_rect = cell_surf.get_rect(center=(315, 315))
        screen.blit(cell_surf, cell_rect)
        pygame.display.flip()

    # Regular game drawing
    else:
        screen.fill((255, 255, 255))  # Clear the screen
        board.draw()                  # Draw the Sudoku board
        draw_reset_button(screen, butt1_surface, butt_rect1)  # Draw the reset button
        draw_restart_button(screen, butt2_surface, butt_rect2)# **Draw the restart button**
        draw_exit_button(screen, butt3_surface, butt_rect3)
        board.draw_cell()             # Highlight selected cell
        if clicked:
            board.select(row, col)
        pygame.display.flip()
