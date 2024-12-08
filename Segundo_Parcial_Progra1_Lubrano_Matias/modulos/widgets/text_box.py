import pygame as pg
from .widget import Widget
from ..variables import SONIDO_CLICK

class TextBox(Widget):
    
    def __init__(self, x, y, texto, pantalla, font_size = 25, on_click = None, on_click_param = None):
        super().__init__(x, y, texto, pantalla, font_size)
        self.font = pg.font.Font('assets/fonts/fuente_comica.ttf', self.font_size)
        self.image = self.font.render(self.texto, True, (255, 255, 255))
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.click_option_sfx = pg.mixer.Sound(SONIDO_CLICK)
        self.click_option_sfx.set_volume(0.3)
        
        self.on_click = on_click
        self.on_click_param = on_click_param
        
        self.write_on = True
        self.writing = ''
        self.image_writing = self.font.render(self.writing, True, (255, 255, 255))
        self.rect_writing = self.image_writing.get_rect()
        self.rect_writing.center = (x, y)
    
    def write_on_box(self, event_list: list):
        for evento in event_list:
            if evento.type == pg.KEYDOWN and self.write_on:
                if evento.key == pg.K_BACKSPACE:
                    self.writing = self.writing[:-1]
                else:
                    self.writing += evento.unicode
                self.click_option_sfx.play()
    
    def draw(self):
        super().draw()
        self.image.blit(self.pantalla, (self.rect_writing.x, self.rect_writing.y))
    
    def update(self, event_list: list):
        self.draw()
        self.write_on_box(event_list)