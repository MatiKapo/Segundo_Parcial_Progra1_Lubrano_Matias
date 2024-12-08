import sys
import pygame as pg

from modulos.forms import (
    FormManager
)
from modulos.variables import DIMENSION_PANTALLA
from modulos.auxiliar import cargar_ranking

def iniciar_juego():
    pg.init()

    pantalla = pg.display.set_mode(DIMENSION_PANTALLA, pg.SCALED)
    pg.display.set_caption('Juego Mati UTN')
    
    juego_andando = True
    
    forms = FormManager(pantalla)
    
    while juego_andando:
        event_list = pg.event.get()
        for event in event_list:
            if event.type == pg.QUIT:
                juego_andando = False
        
        forms.update(event_list)
        pg.display.update()
        
    pg.quit()
    sys.exit()