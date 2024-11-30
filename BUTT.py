butt1_surface = pygame.Surface(80, 30)
text_butt1 = font.render("RESET", True, (0, 0, 0))
text_rect1 = text.get_rect1(center=(button_surface.get_width() / 2, button_surface.get_height() / 2))
butt_rect1 = pygame.Rect(65, 650, 80, 30)
screen.fill(255, 192, 203)
butt_surface.blit(text_butt1, text_rect1)
screen.blit(butt1_surface, (butt_rect1.x, butt_rect1.y))


