
# #easy: y --> 157.5

import pygame
FONT = 35

def create_easy_button():
    button1_font = pygame.font.Font(None, FONT)


    button1_surface = pygame.Surface((100,50))
    button1_surface.fill((255, 192, 203))  # Pink button background

    # Render the "RESET" text
    text_button1 = button1_font.render("Easy", True, (0,0,0))  # Black text
    text_rectangle1 = text_button1.get_rect(center=(button1_surface.get_width() / 2,button1_surface.get_height() / 2))
    button1_surface.blit(text_button1, text_rectangle1)

    # Define the button rectangle for interaction
    button_rectangle1 = pygame.Rect(130, 405, 100, 50)


    return button1_surface, button_rectangle1


def create_medium_button():
    button2_font = pygame.font.Font(None, FONT)

    button2_surface = pygame.Surface((100,50))
    button2_surface.fill((255, 192, 203))  # Pink button background

    # Render the "RESET" text
    text_button2 = button2_font.render("Medium", True, (0,0,0))  # Black text
    text_rectangle2 = text_button2.get_rect(center=(button2_surface.get_width() / 2,button2_surface.get_height() / 2))
    button2_surface.blit(text_button2, text_rectangle2)

    # Define the button rectangle for interaction
    button_rectangle2 = pygame.Rect(265, 405, 100, 50)


    return button2_surface, button_rectangle2

def create_hard_button():
    button3_font = pygame.font.Font(None, FONT)

    button3_surface = pygame.Surface((100,50))
    button3_surface.fill((255, 192, 203))  # Pink button background

    # Render the "RESET" text
    text_button3 = button3_font.render("Hard", True, (0,0,0))  # Black text
    text_rectangle3 = text_button3.get_rect(center=(button3_surface.get_width() / 2,button3_surface.get_height() / 2))
    button3_surface.blit(text_button3, text_rectangle3)

    # Define the button rectangle for interaction
    button_rectangle3 = pygame.Rect(400, 405, 100, 50)


    return button3_surface, button_rectangle3



def create_exit2_button():
    button4_font = pygame.font.Font(None, FONT)
    button4_surface = pygame.Surface((100, 75))
    button4_surface.fill((255, 192, 203))  # Pink button background

    # Render the "RESET" text
    text_button4 = button4_font.render("EXIT", True, (0, 0, 0))  # Black text
    text_rectangle4 = text_button4.get_rect(center=(button4_surface.get_width() / 2, button4_surface.get_height() / 2))
    button4_surface.blit(text_button4, text_rectangle4)


    button_rectangle4 = pygame.Rect(315, 315, 150, 100)

    return button4_surface, button_rectangle4

def create_restart2_button():
    button5_font = pygame.font.Font(None, FONT)
    button5_surface = pygame.Surface((100, 75))
    button5_surface.fill((255, 192, 203))  # Pink button background

    # Render the "RESET" text
    text_button5 = button5_font.render("RESTART", True, (0, 0, 0))  # Black text
    text_rectangle5 = text_button5.get_rect(center=(button5_surface.get_width() / 2, button5_surface.get_height() / 2))
    button5_surface.blit(text_button5, text_rectangle5)

    # Define the button rectangle
    button_rectangle5 = pygame.Rect(275, 650, 80, 30)

    return button5_surface, button_rectangle5





