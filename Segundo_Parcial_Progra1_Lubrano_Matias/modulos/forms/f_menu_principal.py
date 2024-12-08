import pygame as pg
from .form import Form
from ..widgets import (
    Button, TextTitle
)
from ..variables import DIMENSION_PANTALLA, FONDO_MENU

class FormMenu(Form):
    
    def __init__(self, name, pantalla, x, y, active, level_num, music_path):
        super().__init__(name, pantalla, x, y, active, level_num, music_path)
             
        self.surface = pg.image.load(FONDO_MENU).convert_alpha()
        self.surface = pg.transform.scale(self.surface, DIMENSION_PANTALLA)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        
        self.titulo_menu = TextTitle(x = DIMENSION_PANTALLA[0]//2 + 8, y = DIMENSION_PANTALLA[1]//2 - 255, texto = 'THIS   THAT', pantalla = pantalla, font_size = 75)
        self.subtitulo_menu = TextTitle(x = DIMENSION_PANTALLA[0]//2 - 22, y = DIMENSION_PANTALLA[1]//2 - 200, texto = 'JUEGO    MATI', pantalla = pantalla, font_size = 35)
          
        self.boton_iniciar = Button(x = DIMENSION_PANTALLA[0]//2 - 80, y = DIMENSION_PANTALLA[1]//2 - 40, texto = 'JUGAR', pantalla = pantalla, on_click = self.click_iniciar, on_click_param='f_reglas', font_size = 35)
        self.boton_opciones = Button(x = DIMENSION_PANTALLA[0]//2 + 87, y = DIMENSION_PANTALLA[1]//2 + 35, texto = 'OPCIONES', pantalla = pantalla, on_click = self.click_opciones, on_click_param = 'f_opciones', font_size = 35)
        self.boton_ranking = Button(x = DIMENSION_PANTALLA[0]//2 - 95, y = DIMENSION_PANTALLA[1]//2 + 110, texto = 'RANKING', pantalla = pantalla, on_click = self.click_ranking, on_click_param = 'f_ranking', font_size = 35)
        self.boton_salir = Button(x = DIMENSION_PANTALLA[0]//2 + 50, y = DIMENSION_PANTALLA[1]//2 + 185, texto = 'SALIR', pantalla = pantalla, on_click = self.click_salir, font_size = 35)

        self.widget_list = [
            self.subtitulo_menu, self.titulo_menu, self.boton_salir, 
            self.boton_opciones, self.boton_ranking, self.boton_iniciar
        ]
        self.music_update()
    
    def click_iniciar(self, parametro):
        self.set_active(parametro)
    
    def click_opciones(self, parametro):
        self.set_active(parametro)
    
    def click_ranking(self, parametro):
        self.set_active(parametro)

    def click_salir(self, parametro):
        self.set_active(parametro)
    
    def draw(self):
        super().draw()
        for widget in self.widget_list:
            widget.draw()
    
    def update(self):
        self.draw()
        for widget in self.widget_list:
            widget.update()