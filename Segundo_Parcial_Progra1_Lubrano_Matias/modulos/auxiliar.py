import pygame as pg
import json
from .variables import RANKING


def sort_matrix(matrix: list[list]):
    
    for i in range(len(matrix) - 1):
        for j in range(i+1, len(matrix)):
            if int(matrix[i][1]) < int(matrix[j][1]):
                matrix[i], matrix[j] =\
                matrix[j], matrix[i]

def cargar_ranking():
    ranking = []
    with open(RANKING, 'r') as rkng:
        lineas = rkng.read()
        for linea in lineas.split('\n'):
            ranking.append(linea.split(','))
    
    sort_matrix(ranking)
    
    return ranking

def grabar_puntaje(jugador):
    with open(RANKING, '+a') as rkn:
        rkn.write(jugador.to_csv_format())
        print('PUNTAJE GUARDADO CON ÉXITO!')





