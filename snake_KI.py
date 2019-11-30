import pygame as pg, random as rnd
import math
from snake_learn import lernen
screen = pg.display.set_mode([1000, 600])

def diagonaler_abstand(abstand_1, abstand_2):
    diagonale = abstand_1, abstand_2      #abstand_1 und abstand_2 werden auf die kleinere Zahl wird reduziert, die dann auch der Diagonale entspricht.
    sortierte_diagonale = sorted(diagonale)
    layer = sortierte_diagonale[0]
    return layer

def wand_layer(richt_x, richt_y, score, tempo, snake, bonus_x, bonus_y, GRÖßE, BREITE, HÖHE, x, y):
    l_1 = y / GRÖßE
    l_2 = (BREITE - x) / GRÖßE
    l_3 = (HÖHE - y) / GRÖßE
    l_4 = x / GRÖßE
    l_5 = diagonaler_abstand(l_1, l_2)
    l_6 = diagonaler_abstand(l_2, l_3)
    l_7 = diagonaler_abstand(l_3, l_4)
    l_8 = diagonaler_abstand(l_4, l_1)
    #ki_steuerung = snake_body(richt_x, richt_y, score, tempo, snake, bonus_x, bonus_y, GRÖßE, BREITE, HÖHE, x, y, l_1, l_2, l_3, l_4, l_5, l_6, l_7, l_8)
    #return ki_steuerung

def snake_layer(snake):
    kopf = snake[-1]
    kopf_x = kopf[0]
    kopf_y = kopf[1]

    rechts = []
    links = []
    oben = []
    unten = []
    oben_rechts = []
    oben_links = []
    unten_rechts = []
    unten_links =[]


    for (x,y) in snake:
        if x == kopf_x and y <= kopf_y :
            oben.append(kopf_y - y)
        elif x == kopf_x and y >= kopf_y:
            unten.append(y - kopf_y)
        elif y == kopf_y and x <= kopf_x:
            links.append(kopf_x - x)
        elif y == kopf_y and x >= kopf_x:
            rechts.append(x - kopf_x)
        elif x >= kopf_x and y <= kopf_y :
            if (kopf_y - y) == (x - kopf_x):
                oben_rechts.append(math.sqrt((x - kopf_x)*(x - kopf_x) + (kopf_y-y)*(kopf_y-y)))
        elif x <= kopf_x and y <= kopf_y :
            if (kopf_y - y) == (kopf_x - x):
                oben_links.append(math.sqrt((kopf_x - x)*(kopf_x - x) + (kopf_y-y)*(kopf_y-y)))
        elif x <= kopf_x and y >= kopf_y :
            if (y - kopf_y) == (kopf_x - x):
                unten_links.append(math.sqrt((kopf_x - x)*(kopf_x - x) + (y - kopf_y)*(y - kopf_y)))
        elif x >= kopf_x and y >= kopf_y :
            if (y - kopf_y) == (x - kopf_x):
                unten_rechts.append(math.sqrt((x - kopf_x)*(x - kopf_x) + (y - kopf_y)*(y - kopf_y)))
    print(rechts, links, oben, unten, oben_rechts, oben_links, unten_rechts, unten_links)
