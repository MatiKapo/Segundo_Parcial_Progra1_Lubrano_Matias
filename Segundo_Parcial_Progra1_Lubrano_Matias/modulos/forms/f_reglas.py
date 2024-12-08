import pygame as pg
from .form import Form
from ..widgets import (
    Button, TextTitle
)
from ..variables import DIMENSION_PANTALLA, REGLAS_FONDO, REGLAS_IMAGEN, FLECHA_REGLAS

class ReglasJuego(Form):
    
    def __init__(self, name, pantalla, x, y, active, level_num, music_path):
        super().__init__(name, pantalla, x, y, active, level_num, music_path)
        
        self.surface = pg.image.load(REGLAS_FONDO).convert_alpha()
        self.surface = pg.transform.scale(self.surface, DIMENSION_PANTALLA)
        
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y

        self.reglas_titulo = TextTitle(x = DIMENSION_PANTALLA[0]//2 - 210, y = DIMENSION_PANTALLA[1]//2 - 230, texto='REGLAS', pantalla = pantalla, font_size = 75)
        self.reglas_texto_1 = TextTitle(x = DIMENSION_PANTALLA[0]//2 - 218, y = DIMENSION_PANTALLA[1]//2 - 135, texto='- Una Pregunta, dos opciones', pantalla = pantalla, font_size = 25)
        self.reglas_texto_2 = TextTitle(x = DIMENSION_PANTALLA[0]//2 - 210, y = DIMENSION_PANTALLA[1]//2 - 70, texto='- Si coincides con la mayoría del publico, avanzas', pantalla = pantalla, font_size = 15)
        self.reglas_texto_3 = TextTitle(x = DIMENSION_PANTALLA[0]//2 - 240, y = DIMENSION_PANTALLA[1]//2 - 10, texto='- Si fallas o se termina el tiempo, pierdes', pantalla = pantalla, font_size = 15)
        self.reglas_texto_4 = TextTitle(x = DIMENSION_PANTALLA[0]//2 - 10, y = DIMENSION_PANTALLA[1]//2 + 50, texto='- Comodines: Presiona N para avanzar de pregunta, y R para cambiar de pregunta (UN SOLO USO)', pantalla = pantalla, font_size = 17)
        self.boton_jugar = Button(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2 + 230, texto = 'JUGAR', pantalla=pantalla, on_click=self.click_jugar, on_click_param = 'f_juego', font_size = 75)

        self.widget_list = [self.reglas_titulo, self.reglas_texto_1, self.reglas_texto_2, self.reglas_texto_3, self.reglas_texto_4, self.boton_jugar]
        

    def click_jugar(self, parametro):
        self.set_active(parametro)

    def draw(self):
        super().draw()
        for widget in self.widget_list:
            widget.draw()

        imagen_reglas = pg.image.load(REGLAS_IMAGEN)
        imagen_reglas = pg.transform.smoothscale(imagen_reglas, (400, 300))
        self.pantalla.blit(imagen_reglas,(DIMENSION_PANTALLA[0]//2, DIMENSION_PANTALLA[1]//2 - 300))

        flecha_reglas = pg.image.load(FLECHA_REGLAS)
        flecha_reglas = pg.transform.smoothscale(flecha_reglas, (130, 100))
        self.pantalla.blit(flecha_reglas,(DIMENSION_PANTALLA[0]//2 - 50, DIMENSION_PANTALLA[1]//2 + 80))

        
    def update(self):
        super().draw()
        for widget in self.widget_list:
            widget.update()




