import pygame as pg
import random
from ..jugador import Jugador
from .form import Form
from ..variables import DIMENSION_PANTALLA, FONDO_JUEGO, TELE, BANDERA, RELOJ, BARRA, ESTRELLAS, NEXT, RELOAD

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (139, 0, 0) 
AZUL = (0, 0, 139) 

banco_preguntas = [
    {"pregunta": "¿Cual es un lenguaje interpretado?", "opciones": ["Python", "C++"], "respuesta_correcta": "Python"},
    {"pregunta": "¿En que año fue lanzado Python?", "opciones": ["1985", "1991"], "respuesta_correcta": "1991"},
    {"pregunta": "¿Que tipo de dato es 5.25?", "opciones": ["Int", "Float"], "respuesta_correcta": "Float"},
    {"pregunta": "¿Cual es una variable inmutable?", "opciones": ["Str", "List"], "respuesta_correcta": "Str"},
    {"pregunta": "¿Cual es un archivo binario?", "opciones": ["CSV", "JPG"], "respuesta_correcta": "JPG"},
    {"pregunta": "¿Cual abre un archivo binario para lectura?", "opciones": ["wb", "rb"], "respuesta_correcta": "rb"},
    {"pregunta": "¿Cual es el nombre del creador de Python?", "opciones": ["Guido", "Jake"], "respuesta_correcta": "Guido"},
    {"pregunta": "¿Que formato no se puede guardar en PyGame?", "opciones": ["JPEG", "GIF"], "respuesta_correcta": "GIF"},
    {"pregunta": "¿Cual representa la variable Y en (10, 20)?", "opciones": ["20", "10"], "respuesta_correcta": "20"},
    {"pregunta": "¿En que pais se creo Python?", "opciones": ["Holanda", "Inglaterra"], "respuesta_correcta": "Holanda"}
]

progreso_jugador = {"nivel_actual": 0, "puntos_acumulados": 0}

BOTON_RADIO = 30
BOTON_ROJO_POS = (DIMENSION_PANTALLA[0] // 2 - 160, DIMENSION_PANTALLA[1] // 2 + 245)
BOTON_AZUL_POS = (DIMENSION_PANTALLA[0] // 2 + 160, DIMENSION_PANTALLA[1] // 2 + 245)

estado_comodines = {"n_usado": False, "r_usado": False}


class IniciarJuego(Form):

    def __init__(self, name, pantalla, x, y, active, level_num, music_path):
        super().__init__(name, pantalla, x, y, active, level_num, music_path)
        self.surface = pg.image.load(FONDO_JUEGO).convert_alpha()
        self.surface = pg.transform.scale(self.surface, DIMENSION_PANTALLA)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y

        self.respuesta_jugador = None
        self.panel_votos = None
        self.revelar_colores = False
        self.puntaje_nivel = 0
        self.jugador = Jugador.get_jugador()
        self.progreso = progreso_jugador

    def draw(self):

        self.pantalla.blit(self.surface, (0, 0))

        tele = pg.image.load(TELE)
        tele = pg.transform.smoothscale(tele, (500, 350))
        self.pantalla.blit(tele, (DIMENSION_PANTALLA[0] // 2 - 250, DIMENSION_PANTALLA[1] // 2 - 135))

        barra = pg.image.load(BARRA)
        barra = pg.transform.smoothscale(barra, (860, 80))
        self.pantalla.blit(barra, (DIMENSION_PANTALLA[0]//2 - 430, DIMENSION_PANTALLA[1]//2 - 190))

        estrellas = pg.image.load(ESTRELLAS)
        estrellas = pg.transform.smoothscale(estrellas, (150, 70))
        self.pantalla.blit(estrellas, (DIMENSION_PANTALLA[0]//2 - 400, DIMENSION_PANTALLA[1]//2 - 280))

        bandera = pg.image.load(BANDERA)
        bandera = pg.transform.smoothscale(bandera, (230, 125))
        self.pantalla.blit(bandera, (DIMENSION_PANTALLA[0] // 2 - 400, DIMENSION_PANTALLA[1] // 2 - 80))
        
        bandera_2 = pg.image.load(BANDERA)
        bandera_2 = pg.transform.smoothscale(bandera, (250, 135))
        self.pantalla.blit(bandera_2, (DIMENSION_PANTALLA[0] // 2 - 400, DIMENSION_PANTALLA[1] // 2 + 60))

        reloj = pg.image.load(RELOJ)
        reloj = pg.transform.smoothscale(reloj, (200, 115))
        self.pantalla.blit(reloj, (DIMENSION_PANTALLA[0]//2 + 210, DIMENSION_PANTALLA[1]//2 - 300))

        next = pg.image.load(NEXT)
        next = pg.transform.smoothscale(next, (100, 50))
        self.pantalla.blit(next, (DIMENSION_PANTALLA[0]//2 + 300, DIMENSION_PANTALLA[1]//2 - 30))

        reload = pg.image.load(RELOAD)
        reload = pg.transform.smoothscale(reload, (100, 50))
        self.pantalla.blit(reload, (DIMENSION_PANTALLA[0]//2 + 300, DIMENSION_PANTALLA[1]//2 + 30))

        pg.draw.circle(self.pantalla, NEGRO, BOTON_ROJO_POS, BOTON_RADIO + 3)
        pg.draw.circle(self.pantalla, NEGRO, BOTON_AZUL_POS, BOTON_RADIO + 3)
        pg.draw.circle(self.pantalla, ROJO, BOTON_ROJO_POS, BOTON_RADIO)
        pg.draw.circle(self.pantalla, AZUL, BOTON_AZUL_POS, BOTON_RADIO)

        self.mostrar_texto(f"{self.progreso['puntos_acumulados']}", DIMENSION_PANTALLA[0] // 2 - 320, 40, color = NEGRO)


    def update(self):

        pregunta = banco_preguntas[self.progreso["nivel_actual"]]
        self.panel_votos = self.generar_votos()
        self.revelar_colores = False
        self.respuesta_jugador = None

        tiempo_limite = 15000 
        tiempo_inicio = pg.time.get_ticks()

        while True:

            self.preguntas_restantes = progreso_jugador["nivel_actual"]
            tiempo_actual = pg.time.get_ticks()
            tiempo_restante = tiempo_limite - (tiempo_actual - tiempo_inicio)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_n: 
                         if not estado_comodines["n_usado"]:
                             estado_comodines["n_usado"] = True               
                             self.progreso["nivel_actual"] += 1
                             self.progreso["puntos_acumulados"] += 100
                           
                             return
                    elif event.key == pg.K_r:
                          if not estado_comodines["r_usado"]:
                             estado_comodines["r_usado"] = True                                                
                             self.progreso["nivel_actual"] = random.randint(0, len(banco_preguntas) - 1)
                             return

            self.draw()

            self.mostrar_texto(f"{pregunta['pregunta']}", 150, 134, BLANCO)
            self.mostrar_texto(f"1. {pregunta['opciones'][0]}", 12, 255, ROJO)
            self.mostrar_texto(f"2. {pregunta['opciones'][1]}", 12, 290, AZUL)

            if tiempo_restante > 0:
                segundos_restantes = tiempo_restante // 1000
                self.mostrar_texto(f"{segundos_restantes}", DIMENSION_PANTALLA[0] - 72, DIMENSION_PANTALLA[1]//2 - 263, NEGRO)
            else:
              
                self.progreso["nivel_actual"] = 0
                self.jugador.set_puntaje(self.progreso["puntos_acumulados"])    
                self.progreso["puntos_acumulados"] = 0
                self.set_active("f_ingrese_nombre")
                return

       
            self.dibujar_panel()
            posicion_mouse = pg.mouse.get_pos()

            if self.respuesta_jugador is None and self.verificar_click_mouse(posicion_mouse):
                self.revelar_colores = True

            if self.revelar_colores:
                self.dibujar_panel()
                self.mostrar_porcentajes() 
                pg.display.update()
                pg.time.wait(2000)

                respuesta_correcta = max(set(self.panel_votos), key = self.panel_votos.count)

                if self.respuesta_jugador == respuesta_correcta:

                    if self.preguntas_restantes == 9:

                        self.progreso["puntos_acumulados"] += 100
                        self.jugador.set_puntaje(self.progreso["puntos_acumulados"])
                        self.progreso["nivel_actual"] = 0
                        self.progreso["puntos_acumulados"] = 0
                        self.set_active("f_ingrese_nombre")
                    
                    else: 

                        self.progreso["nivel_actual"] += 1
                        self.progreso["puntos_acumulados"] += 100
                   
                else:
                    self.jugador.set_puntaje(self.progreso["puntos_acumulados"])
                    self.progreso["nivel_actual"] = 0
                    self.progreso["puntos_acumulados"] = 0
                    self.set_active("f_ingrese_nombre")
                    return
                break

            pg.display.update()

    def generar_votos(self):
        return [random.choice(["Rojo", "Azul"]) for i in range(16)]

    def dibujar_panel(self):

        cuadritos_x = (DIMENSION_PANTALLA[0]//2 - 160)
        cuadritos_y = (DIMENSION_PANTALLA[1]//2 - 160)

        for i in range(16):

            if not self.revelar_colores:
                color = NEGRO
            else:
                if self.panel_votos[i] == "Rojo":
                    color = ROJO
                else:
                    color = AZUL
            
            x = cuadritos_x + (i % 4) * 80
            y = cuadritos_y + (i // 4) * 45
            pg.draw.rect(self.pantalla, color, (x + 5, y + 90, 70, 37))

    def mostrar_porcentajes(self):
        total_votos = len(self.panel_votos)
        votos_rojo = self.panel_votos.count("Rojo")
        votos_azul = self.panel_votos.count("Azul")
        porcentaje_rojo = (votos_rojo / total_votos) * 100
        porcentaje_azul = (votos_azul / total_votos) * 100

        self.mostrar_texto(f"Rojo: {porcentaje_rojo:} %", 12, 400, ROJO)
        self.mostrar_texto(f"Azul: {porcentaje_azul:} %", 12, 435, AZUL)

    def verificar_click_mouse(self, pos):
        if pg.mouse.get_pressed()[0]: 
            if pg.Rect(BOTON_ROJO_POS[0] - BOTON_RADIO, BOTON_ROJO_POS[1] - BOTON_RADIO, BOTON_RADIO * 2, BOTON_RADIO * 2).collidepoint(pos):
                self.respuesta_jugador = "Rojo"
                return True
            elif pg.Rect(BOTON_AZUL_POS[0] - BOTON_RADIO, BOTON_AZUL_POS[1] - BOTON_RADIO, BOTON_RADIO * 2, BOTON_RADIO * 2).collidepoint(pos):
                self.respuesta_jugador = "Azul"
                return True
        return False

    def mostrar_texto(self, texto, x, y, color = NEGRO):
        font = pg.font.SysFont('Arial', 30) # aca le puse arial porque no me tomaba la fuente que subi, no se porque
        texto = font.render(texto, True, color)
        self.pantalla.blit(texto, (x, y))
