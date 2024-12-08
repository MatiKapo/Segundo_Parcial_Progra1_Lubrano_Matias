import pygame as pg
from .widget import Widget



class TextTitle(Widget):
    
    def __init__(self, x, y, texto, pantalla, font_size = 50):
        super().__init__(x, y, texto, pantalla, font_size)
        self.font = pg.font.Font('assets/fonts/fuente_comica.ttf', self.font_size)
        self.image = self.font.render(self.texto, True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def draw(self):
        super().draw()
    
    def update(self):
        self.draw()