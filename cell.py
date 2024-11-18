import pygame
class Cell:
    def __init__(self, value, row, col, screen):
        self.value=value
        self.row=row
        self.col=col
        self.screen=screen
    def set_cell_value(self,value):
        self.value=value
    def set_sketched_value(self, value):
        if value==0:
            return ""
        else:
            return value
    def draw(self):
        sketched_value=self.set_sketched_value(self.value)
        self.screen.blit(sketched_value,sketched_value.get_rect(topleft=(SCREEN_SIZE//9*self.row, SCREEN_SIZE//9*self.col)))


