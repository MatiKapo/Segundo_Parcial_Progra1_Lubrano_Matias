import pygame as pg
from ..variables import MUSICA


from .f_menu_principal import FormMenu
from .f_ranking import FormRanking
from .f_opciones import FormOpciones
from .f_ingrese_nombre import FormIngreseNombre
from .f_juego import IniciarJuego
from .f_reglas import ReglasJuego




class FormManager:
    
    def __init__(self, pantalla):
        
        self.main_screen = pantalla
                   
        self.forms = [
            FormMenu(name = 'f_menu_principal', pantalla = self.main_screen, x = 0, y = 0, active = True, level_num = 1, music_path = MUSICA),
            FormRanking(name = 'f_ranking', pantalla = self.main_screen, x = 0, y = 0, active = True, level_num = 1, music_path = MUSICA),
            FormOpciones(name = 'f_opciones', pantalla = self.main_screen, x = 0, y = 0, active = True, level_num = 1, music_path = MUSICA),
            FormIngreseNombre(name = "f_ingrese_nombre", pantalla = self.main_screen, x = 0, y = 0, active = True, level_num = 1, music_path = MUSICA),
            IniciarJuego(name = "f_juego", pantalla = self.main_screen, x = 0, y = 0, active = True, level_num = 1, music_path = MUSICA),
            ReglasJuego(name = "f_reglas", pantalla = self.main_screen, x = 0, y = 0, active = True, level_num = 1, music_path = MUSICA)      
        ]
    
    def forms_update(self, event_list: list):
        
        if self.forms[0].active:
            self.forms[0].update()
            self.forms[0].draw()
            
        elif self.forms[1].active:
            self.forms[1].update()
            self.forms[1].draw()
        
        elif self.forms[2].active:
            self.forms[2].update()
            self.forms[2].draw()
                      
        elif(self.forms[3].active):
            self.forms[3].update(event_list)
            self.forms[3].draw()

        elif(self.forms[4].active):
            self.forms[4].update()
            self.forms[4].draw()

        elif(self.forms[5].active):
            self.forms[5].update()
            self.forms[5].draw()
        
        
        
        
    
    def update(self, event_list: list):
        self.forms_update(event_list)