import pygame as pg, random as rnd
from snake_learn import lernen
screen = pg.display.set_mode([1000, 600])

def diagonaler_abstand(abstand_1, abstand_2):
    diagonale = abstand_1, abstand_2      #abstand_1 und abstand_2 werden auf die kleinere Zahl wird reduziert, die dann auch der Diagonale entspricht.
    sortierte_diagonale = sorted(diagonale)
    layer = sortierte_diagonale[0]
    return layer

def wand_layer(richt_x, richt_y, score, tempo, snake, bonus_x, bonus_y, GRÖßE, BREITE, HÖHE):
    kopf = snake[-1]
    kopf_x = kopf[0]
    kopf_y = kopf[1]

    layer_1 = kopf_y / GRÖßE
    layer_2 = (BREITE - kopf_x) / GRÖßE
    layer_3 = (HÖHE - kopf_y) / GRÖßE
    layer_4 = kopf_x / GRÖßE
    layer_5 = diagonaler_abstand(layer_1, layer_2)
    layer_6 = diagonaler_abstand(layer_2, layer_3)
    layer_7 = diagonaler_abstand(layer_3, layer_4)
    layer_8 = diagonaler_abstand(layer_4, layer_1)
    ki_steuerung = lernen(layer_1, layer_2, layer_3, layer_4, layer_5, layer_6, layer_7, layer_8)
    return ki_steuerung

def snake_layer(snake):
    kopf = snake[-1]
    kopf_x = kopf[0]
    kopf_y = kopf[1]

    print(kopf)

    for (x,y) in snake:
        if x == kopf_x and y <= kopf_y :
            print("oben: ", kopf_y - y)
