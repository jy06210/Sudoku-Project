import pygame, sys
from pygame import MOUSEBUTTONDOWN
from BUTT import create_reset_button, draw_reset_button, create_restart_button, draw_restart_button, draw_exit_button, create_exit_button
from sudoku_generator import *
from board import *
from cell import *
from Constants import *
from Home_BUTTon import *

pygame.init()

game_over = False
screen = pygame.display.set_mode((630, 700))
pygame.display.set_caption("Sudoku")

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if start_screen:
            screen.fill((255, 255, 255))
            background = pygame.image.load("Untitled design.png")
            screen.blit(background, background.get_rect(topleft=(0, 0)))
            sketched_value = "Welcome to Sudoku"
            value_font = pygame.font.Font(None, 80)
            cell_surf = value_font.render(sketched_value, 0, (255, 255, 255))
            cell_rect = cell_surf.get_rect(center=(315, 240))
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
                    start_screen = False
                    sudoku_board, correct_board = generate_sudoku(9, num_removed)
                    answer = correct_board
                    board = Board(630, 630, screen, 1, 9, num_removed, sudoku_board)
                elif button_rectangle2.collidepoint(event.pos):
                    num_removed = 40
                    start_screen = False
                    sudoku_board, correct_board = generate_sudoku(9, num_removed)
                    answer = correct_board
                    board = Board(630, 630, screen, 1, 9, num_removed, sudoku_board)
                elif button_rectangle3.collidepoint(event.pos):
                    num_removed = 50
                    start_screen = False
                    sudoku_board, correct_board = generate_sudoku(9, num_removed)
                    answer = correct_board
                    board = Board(630, 630, screen, 1, 9, num_removed, sudoku_board)

        if event.type == MOUSEBUTTONDOWN and not start_screen:
            if butt_rect1.collidepoint(event.pos):
                board.reset_to_original()
                clicked = False
            elif butt_rect2.collidepoint(event.pos):
                start_screen=True
            elif butt_rect3.collidepoint(event.pos):
                sys.exit()
            elif not game_over:
                x, y = event.pos
                result = board.click(x, y)
                if result is not None:
                    row, col = result
                    clicked = True

        if event.type == pygame.KEYDOWN and clicked and not start_screen:
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

        if game_over and not start_screen:
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
    if game_over:
        board.draw_cell()
        pygame.display.flip()
        pygame.time.delay(1000)
        if board.is_full():
            correct = board.check_board(answer)
        board.reset_to_original()
        screen.fill((255, 255, 255))
        background = pygame.image.load("Untitled design.png")
        sketched_value = "Game Won!" if correct else "Game Over :(!"
        fontty = 100
        value_font = pygame.font.Font(None, fontty)
        cell_surf = value_font.render(sketched_value, 0, (0, 0, 0))
        cell_rect = cell_surf.get_rect(center=(315, 315))
        screen.blit(cell_surf, cell_rect)
        if sketched_value == "Game Won!":
            screen.blit(button4_surface, button_rectangle4.topleft)
            if event.type == MOUSEBUTTONDOWN:
                if button_rectangle4.collidepoint(event.pos):
                    sys.exit()
        else:
            screen.blit(button5_surface, button_rectangle5.topleft)
            if button_rectangle5.collidepoint(event.pos):
                start_screen = True
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

        else:
            if not start_screen:
                screen.fill((255, 255, 255))
                board.draw()
                draw_reset_button(screen, butt1_surface, butt_rect1)
                draw_restart_button(screen, butt2_surface, butt_rect2)
                draw_exit_button(screen, butt3_surface, butt_rect3)
                board.draw_cell()
                if clicked:
                    board.select(row, col)
                pygame.display.flip()