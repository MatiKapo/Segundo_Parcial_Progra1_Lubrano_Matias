import pygame as pg
from .form import Form
from ..widgets import (
    Button, TextTitle
)
from ..variables import DIMENSION_PANTALLA, FONDO_MENU

class FormOpciones(Form):
    
    def __init__(self, name, pantalla, x, y, active, level_num, music_path):
        super().__init__(name, pantalla, x, y, active, level_num, music_path)
        
        self.surface = pg.image.load(FONDO_MENU).convert_alpha()
        self.surface = pg.transform.scale(self.surface, DIMENSION_PANTALLA)
        
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        
        self.opciones_titulo = TextTitle(x = DIMENSION_PANTALLA[0]//2 + 8, y = DIMENSION_PANTALLA[1]//2 - 255, texto='THIS   THAT', pantalla = pantalla, font_size = 75)
        self.opciones_subtitulo = TextTitle(x = DIMENSION_PANTALLA[0]//2 - 210, y = DIMENSION_PANTALLA[1]//2 , texto = 'OPCIONES', pantalla = pantalla, font_size = 65)
        
        self.boton_activar_musica = Button(x = DIMENSION_PANTALLA[0]//2 + 190, y = DIMENSION_PANTALLA[1]//2 - 30, texto = 'ACTIVAR MUSICA', pantalla = pantalla, on_click = self.click_activar_musica, font_size = 35)
        self.boton_desactivar_musica = Button(x = DIMENSION_PANTALLA[0]//2 + 190, y=DIMENSION_PANTALLA[1]//2 + 30, texto = 'DESACTIVAR MUSICA', pantalla = pantalla, on_click = self.click_desactivar_musica, font_size = 35)
        
        self.boton_volver = Button(x = DIMENSION_PANTALLA[0]//2 + 190, y = DIMENSION_PANTALLA[1]//2 + 240, texto = 'VOLVER', pantalla = pantalla, on_click=self.click_volver, on_click_param = 'f_menu_principal', font_size = 70)
        self.widget_list = [self.opciones_subtitulo, self.opciones_titulo, self.boton_volver, self.boton_desactivar_musica, self.boton_activar_musica]
        self.music_update()
        
    def click_activar_musica(self, parametro):
        pg.mixer.music.unpause()
    
    def click_desactivar_musica(self, parametro):
        pg.mixer.music.pause()
    
    def click_volver(self, parametro):
        self.set_active(parametro)
    
    def draw(self):
        super().draw()
        for widget in self.widget_list:
            widget.draw()
        
    def update(self):
        super().draw()
        for widget in self.widget_list:
            widget.update()