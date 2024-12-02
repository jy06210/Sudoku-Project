# import pygame
#
# #easy: y --> 157.5
#
# FONT = 50
# def create_medium_button():
#     button2_font = pygame.font.Font(None, FONT)
#     button2_surface = pygame.Surface((315, 430))
#     button2_surface.fill((255, 192, 203))  # Pink button background
#
#     # Render the "RESET" text
#     text_button2 = button2_font.render("Medium", True, (0, 0, 0))  # Black text
#     text_rectangle2 = text_button2.get_rect(center=(button2_surface.get_width() / 2, button2_surface.get_height() / 2))
#     button2_surface.blit(text_button2, text_rectangle2)
#
#     # Define the button rectangle
#     button_rectangle2 = pygame.Rect(265, 405, 100, 50)
#
#     return button2_surface, button_rectangle2
import pygame
FONT = 35
def create_medium_button():
    button2_font = pygame.font.Font(None, FONT)


    button2_surface = pygame.Surface((100,50))
    button2_surface.fill((255, 192, 203))  # Pink button background

    text_button2 = button2_font.render("Medium", True, (0, 0, 0))  # Black text
    text_rectangle2 = text_button2.get_rect(center=(button2_surface.get_width() / 2,button2_surface.get_height() / 2))
    button2_surface.blit(text_button2, text_rectangle2)

    # Define the button rectangle for interaction
    button_rectangle2 = pygame.Rect(265, 405, 100, 50)

    return button2_surface, button_rectangle2
