import pygame as pg
from .form import Form
from ..widgets import Button, TextBox, TextTitle
from ..variables import DIMENSION_PANTALLA, FONDO_MENU
from ..jugador import Jugador
from ..auxiliar import grabar_puntaje

class FormIngreseNombre(Form):
    
    def __init__(self, name, pantalla, x, y, active, level_num, music_path):
        super().__init__(name, pantalla, x, y, active, level_num, music_path)

        self.surface = pg.image.load(FONDO_MENU).convert_alpha()
        self.surface = pg.transform.scale(self.surface, DIMENSION_PANTALLA)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.jugador = Jugador.get_jugador()
        
        self.confirmar_nombre = False
                   
        self.titulo = TextTitle(x = DIMENSION_PANTALLA[0]//2 + 8, y = DIMENSION_PANTALLA[1]//2 - 255, texto = 'THIS   THAT',pantalla = pantalla, font_size = 75)
        self.subtitulo = TextTitle(x = DIMENSION_PANTALLA[0]//2 - 200, y = DIMENSION_PANTALLA[1]//2 - 50, texto = "NOMBRE:", pantalla = pantalla, font_size = 60)
        
        self.barra_escribir = TextBox(x = DIMENSION_PANTALLA[0]//2 - 200, y = DIMENSION_PANTALLA[1]//2 + 80, texto = "________", pantalla = pantalla, font_size = 40)
        self.boton_confirmar = Button(x = DIMENSION_PANTALLA[0]//2 + 190, y = DIMENSION_PANTALLA[1]//2, texto = "CONFIRMAR", pantalla = pantalla, on_click = self.click_confirmar, font_size = 60)
        
        self.widget_list = [self.titulo, self.subtitulo, self.boton_confirmar]

        
    def click_confirmar(self, parametro): 
        
        self.confirmar_nombre = True
        self.jugador.set_nombre(self.texto_escrito.texto)
        print(f'Su nombre: {self.jugador.get_nombre()} - {self.jugador.puntaje_total} puntos')
        grabar_puntaje(self.jugador)
        self.set_active('f_ranking')
        
    def draw(self):
        
        super().draw()
        for widget in self.widget_list:    
            widget.draw()
        self.barra_escribir.draw()
        self.texto_escrito  = TextTitle(x = DIMENSION_PANTALLA[0]//2 - 200, y = DIMENSION_PANTALLA[1]//2 + 70, texto = f"{self.barra_escribir.writing.upper()}",
        pantalla = self.pantalla,font_size = 30)
        self.texto_escrito.draw()

    def update(self,event_list):
        
        super().draw()
        self.barra_escribir.update(event_list)
        for widget in self.widget_list:    
            widget.update()  
