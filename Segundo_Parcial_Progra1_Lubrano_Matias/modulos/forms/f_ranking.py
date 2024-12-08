import pygame as pg
from .form import Form
from ..widgets import  (
    Button, TextTitle
)
from ..variables import DIMENSION_PANTALLA, FONDO_MENU
from ..auxiliar import cargar_ranking

class FormRanking(Form):
    
    def __init__(self, name, pantalla, x, y, active, level_num, music_path):
        super().__init__(name, pantalla, x, y, active, level_num, music_path)
        
        self.surface = pg.image.load(FONDO_MENU).convert_alpha()
        self.surface = pg.transform.scale(self.surface, DIMENSION_PANTALLA)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.confirmar_nombre = True
        
        self.ranking_mostrado = []
        self.ranking_list = []
        
        self.titulo = TextTitle(x = DIMENSION_PANTALLA[0]//2 + 8, y = DIMENSION_PANTALLA[1]//2 - 255, texto = 'THIS   THAT', pantalla = pantalla, font_size=75)
        self.subtitulo = TextTitle(x = DIMENSION_PANTALLA[0]//2 - 210, y = DIMENSION_PANTALLA[1]//2 - 130, texto = 'LOS MEJORES', pantalla = pantalla, font_size = 50)
        self.boton_volver = Button(x = DIMENSION_PANTALLA[0]//2 + 190, y = DIMENSION_PANTALLA[1]//2, texto = 'VOLVER', pantalla = pantalla, on_click = self.click_volver, on_click_param='f_menu_principal', font_size = 70)
        
        self.widget_list = [
            self.titulo, self.subtitulo, self.boton_volver
        ]
        
    
    def init_ranking(self):
        for i in range(len(self.ranking_list)): 

            self.ranking_mostrado.append(TextTitle(x = DIMENSION_PANTALLA[0]//2 - 330, y=DIMENSION_PANTALLA[1]//2.5 + i * 25, texto = f'{i + 1}', pantalla = self.pantalla, font_size = 25))         
            self.ranking_mostrado.append(TextTitle(x = DIMENSION_PANTALLA[0]//2 - 230, y = DIMENSION_PANTALLA[1]//2.5 + i * 25, texto = f'{self.ranking_list[i][0]}', pantalla=self.pantalla, font_size = 25))       
            self.ranking_mostrado.append(TextTitle(x = DIMENSION_PANTALLA[0]//2 - 130, y=DIMENSION_PANTALLA[1]//2.5 + i * 25, texto = f'{self.ranking_list[i][1]}', pantalla = self.pantalla, font_size = 25))
    
    def inicializar_ranking(self):
        self.ranking_list = cargar_ranking()
        self.init_ranking()
    
    def click_volver(self, parametro):
        self.set_active(parametro)
    
    def draw(self):
        super().draw()
        for widget in self.widget_list:
            widget.draw()
        for ranking in self.ranking_mostrado:
            ranking.draw()
    
    def update(self):
        if self.active:
            self.inicializar_ranking()
        super().draw()
        for widget in self.widget_list:
            widget.update()