# import pygame
# from Constants import *
# from sudoku import *
# from sudoku_generator import *
#
#
# butt_font = pygame.font.Font(None, FONT)
#
# butt1_surface = pygame.Surface((80, 30))
#
# text_butt1 = butt_font.render("RESET", True, (0, 0, 0))
#
# text_rect1 = text_butt1.get_rect1(center=(butt1_surface.get_width() / 2, butt1_surface.get_height() / 2))
#
# butt1_surface.fill(255, 192, 203)
# butt1_surface.blit(text_butt1, text_rect1)
#
# butt_rect1 = pygame.Rect(65, 650, 80, 30)
#
# screen.blit(butt1_surface, (butt_rect1.x, butt_rect1.y))
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
# pygame.quit()

import pygame


FONT = 25
def create_reset_button():
    """Creates the reset button surface and its rect."""
    butt_font = pygame.font.Font(None, FONT)
    butt1_surface = pygame.Surface((80, 30))
    butt1_surface.fill((255, 192, 203))  # Pink button background

    # Render the "RESET" text
    text_butt1 = butt_font.render("RESET", True, (0, 0, 0))  # Black text
    text_rect1 = text_butt1.get_rect(center=(butt1_surface.get_width() / 2, butt1_surface.get_height() / 2))
    butt1_surface.blit(text_butt1, text_rect1)

    # Define the button rectangle
    butt_rect1 = pygame.Rect(65, 650, 80, 30)

    return butt1_surface, butt_rect1

def create_restart_button():
    butt_font = pygame.font.Font(None, FONT)
    butt2_surface = pygame.Surface((80, 30))
    butt2_surface.fill((255, 192, 203))  # Pink button background

    # Render the "RESET" text
    text_butt2 = butt_font.render("RESTART", True, (0, 0, 0))  # Black text
    text_rect2 = text_butt2.get_rect(center=(butt2_surface.get_width() / 2, butt2_surface.get_height() / 2))
    butt2_surface.blit(text_butt2, text_rect2)

    # Define the button rectangle
    butt_rect2 = pygame.Rect(275, 650, 80, 30)

    return butt2_surface, butt_rect2

def create_exit_button():
    butt_font = pygame.font.Font(None, FONT)
    butt3_surface = pygame.Surface((80, 30))
    butt3_surface.fill((255, 192, 203))  # Pink button background

    # Render the "RESET" text
    text_butt3 = butt_font.render("EXIT", True, (0, 0, 0))  # Black text
    text_rect3 = text_butt3.get_rect(center=(butt3_surface.get_width() / 2, butt3_surface.get_height() / 2))
    butt3_surface.blit(text_butt3, text_rect3)

    # Define the button rectangle
    butt_rect3 = pygame.Rect(485, 650, 80, 30)

    return butt3_surface, butt_rect3

def draw_reset_button(screen, butt1_surface, butt_rect1):
    """Draws the reset button on the given screen."""
    screen.blit(butt1_surface, (butt_rect1.x, butt_rect1.y))

def draw_restart_button(screen, butt2_surface, butt_rect2):
    screen.blit(butt2_surface, (butt_rect2.x, butt_rect2.y))


def draw_exit_button(screen, butt3_surface, butt_rect3):
    screen.blit(butt3_surface, (butt_rect3.x, butt_rect3.y))




