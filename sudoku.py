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


import pygame, sys
from pygame import MOUSEBUTTONDOWN
from BUTT import create_reset_button, draw_reset_button, create_restart_button, draw_restart_button, draw_exit_button, create_exit_button
from sudoku_generator import *
from board import *
from cell import *
from Constants import *
from Home_BUTTon import *

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
button1_surface, button_rectangle1 = create_easy_button()
button2_surface, button_rectangle2 = create_medium_button()
button3_surface, button_rectangle3 = create_hard_button()
button4_surface, button_rectangle4 = create_exit2_button()
button5_surface, button_rectangle5 = create_restart2_button()

start_screen=True
clicked = False
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            #Handle reset button click
            if butt_rect1.collidepoint(event.pos):
                board.reset_to_original()
                clicked = False
            #Handle restart button click
            elif butt_rect2.collidepoint(event.pos):
                start_screen=True
                # sudoku_board, correct_board = generate_sudoku(9, 6)
                # answer = correct_board
                # board = Board(630, 630, screen, 1, 9, 30, sudoku_board)
                # clicked = False
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
        sketched_value = "Game Won!" if correct else "Game Over :(!"
        sketched_value = "Game Won!" if correct else "Game Lose!"
        value_font = pygame.font.Font(None, FONT)
        cell_surf = value_font.render(sketched_value, 0, (0, 0, 0))
        cell_rect = cell_surf.get_rect(center=(315, 315))
        screen.blit(cell_surf, cell_rect)
        if sketched_value == "Game Won!":
            screen.blit(button4_surface, button_rectangle4.topleft)
        else:
            screen.blit(button5_surface, button_rectangle5.topleft)
        pygame.display.flip()
    elif start_screen:
        screen.fill((255,255,255))
        background=pygame.image.load("Untitled design.png")
        screen.blit(background, background.get_rect(topleft=(0,0)))
        sketched_value="Welcome to Sudoku"
        value_font=pygame.font.Font(None, 80)
        cell_surf=value_font.render(sketched_value, 0, (255, 255, 255))
        cell_rect=cell_surf.get_rect(center=(315,240))
        screen.blit(cell_surf, cell_rect)
        sketched_value = "Select Game Mode:"
        value_font = pygame.font.Font(None, 80)
        cell_surf = value_font.render(sketched_value, 0, (255, 255, 255))
        cell_rect = cell_surf.get_rect(center=(315, 315))
        screen.blit(cell_surf, cell_rect)
        screen.blit(button1_surface, button_rectangle1.topleft)
        screen.blit(button2_surface, button_rectangle2.topleft)
        screen.blit(button3_surface, button_rectangle3.topleft)
        pygame.display.flip()
        if event.type == MOUSEBUTTONDOWN:
            if button_rectangle1.collidepoint(event.pos):
                num_removed = 30
            elif button_rectangle2.collidepoint(event.pos):
                num_removed = 40
            elif button_rectangle3.collidepoint(event.pos):
                num_removed = 50


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