import pygame as pg, random as rnd
from snake_learn import lernen
import math
screen = pg.display.set_mode([1000, 600])

def diagonaler_abstand(abstand_1, abstand_2):
 diagonale = abstand_1, abstand_2      #abstand_1 und abstand_2 werden auf die kleinere Zahl wird reduziert, die dann auch der Diagonale entspricht.
 sortierte_diagonale = sorted(diagonale)
 layer = sortierte_diagonale[0]
 return layer

def körper_main_1(x, y, kopf_x, kopf_y, layer, snake, GRÖßE):
 for (x,y) in snake:
  if x == kopf_x and y <= kopf_y:
   layer.append((kopf_y - y) / GRÖßE)
 return layer

def körper_main_2(x, y, kopf_x, kopf_y, layer, snake, GRÖßE):

 return layer

def layer_apple(bonus_a, bonus_b, a, b, GRÖßE):
 if bonus_a == a and bonus_b > b:
  layer = (bonus_b - b) / GRÖßE
 else:
  layer = 0
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
 ki_steuerung = snake_body(richt_x, richt_y, score, tempo, snake, bonus_x, bonus_y, GRÖßE, BREITE, HÖHE, x, y, l_1, l_2, l_3, l_4, l_5, l_6, l_7, l_8)
 return ki_steuerung

def snake_body(richt_x, richt_y, score, tempo, snake, bonus_x, bonus_y, GRÖßE, BREITE, HÖHE, x, y, l_1, l_2, l_3, l_4, l_5, l_6, l_7, l_8):

 kopf = snake[-1]
 kopf_x = kopf[0]
 kopf_y = kopf[1]

 l_9 = [0]
 l_10 = [0]
 l_11 = [0]
 l_12 = [0]
 l_13 = [0]
 l_14 = [0]
 l_15 = [0]
 l_16 = [0]

 for (x,y) in snake:
  if x == kopf_x and y <= kopf_y:
   l_9.append((kopf_y - y) / GRÖßE)
 l_9 = float(l_9[-2])

 for (x,y) in snake:
  if y == kopf_y and x <= kopf_x:
   l_10.append((kopf_x - x) / GRÖßE)
 l_10 = float(l_10[-2])

 for (x,y) in snake:
  if x == kopf_x and kopf_y <= y:
   l_11.append((y - kopf_y) / GRÖßE)
 l_11 = float(l_11[-2])

 for (x,y) in snake:
  if y == kopf_y and kopf_x <= x:
   l_12.append((x - kopf_x) / GRÖßE)
 l_12 = float(l_12[-2])


 for (x,y) in snake:
  if x >= kopf_x and y <= kopf_y:
   if (kopf_y - y) == (x - kopf_x):
    l_13.append(math.sqrt(((((x - kopf_x) * (x - kopf_x) + (kopf_y - y) * (kopf_y - y))) / GRÖßE) ** 2) // GRÖßE)
 l_13 = float(l_13[-2])


 for (x,y) in snake:
  if x >= kopf_x and y >= kopf_y:
   if (y - kopf_y) == (x - kopf_x):
    l_14.append(math.sqrt(((((x - kopf_x) * (x - kopf_x) + (y - kopf_y) * (y - kopf_y))) / GRÖßE) ** 2) // GRÖßE)
 l_14 = float(l_14[-2])

 for (x,y) in snake:
  if x <= kopf_x and y >= kopf_y:
   if (y - kopf_y) == (kopf_x - x):
    l_15.append(math.sqrt(((((kopf_x - x) * (kopf_x - x) + (y - kopf_y) * (y - kopf_y))) / GRÖßE) ** 2) // GRÖßE)
 l_15 = float(l_15[-2])


 for (x,y) in snake:
  if x <= kopf_x and y <= kopf_y:
   if (kopf_y - y) == (kopf_x - x):
    l_16.append(math.sqrt(((((kopf_x - x) * (kopf_x - x) + (kopf_y - y) * (kopf_y - y))) / GRÖßE) ** 2) // GRÖßE)
 l_16 = float(l_16[-2])

 #print(l_9, l_10, l_12, l_13, l_14, l_15, l_16)

 ki_steuerung = food(kopf_x, kopf_y, richt_x, richt_y, score, tempo, snake, bonus_x, bonus_y, GRÖßE, BREITE, HÖHE, x, y, l_1, l_2, l_3, l_4, l_5, l_6, l_7, l_8, l_9, l_10, l_12, l_13, l_14, l_15, l_16)
 return ki_steuerung

def food(kopf_x, kopf_y, richt_x, richt_y, score, tempo, snake, bonus_x, bonus_y, GRÖßE, BREITE, HÖHE, x, y, l_1, l_2, l_3, l_4, l_5, l_6, l_7, l_8, l_9, l_10, l_12, l_13, l_14, l_15, l_16):
 l_17 = layer_apple(bonus_x, bonus_y, x, y, GRÖßE)
 l_18 = layer_apple(bonus_y, x, y, bonus_x, GRÖßE)
 l_19 = layer_apple(bonus_x, y, x, bonus_y, GRÖßE)
 l_20 = layer_apple(bonus_y, bonus_x, y, x, GRÖßE)

 l_21 = [0]
 l_22 = [0]
 l_23 = [0]
 l_24 = [0]

 if bonus_x >= kopf_x and bonus_y <= kopf_y:
  if (kopf_y - bonus_y) == (bonus_x - kopf_x):
   l_21.append(math.sqrt((x - bonus_x) * (x - bonus_x) + (bonus_y - y) * (bonus_y - y) // 28))
   l_21 = (l_21[-1] // GRÖßE) + 1

 if x <= bonus_x and y <= bonus_y:
  if (bonus_y - y) == (bonus_x - x):
   l_22.append(math.sqrt((bonus_x - x) * (bonus_x - x) + (bonus_y - y) * (bonus_y - y) // 28))
   l_22 = (l_22[-1] // GRÖßE) + 1

 if x <= bonus_x and y >= bonus_y:
  if (y - bonus_y) == (bonus_x - x):
   l_23.append(math.sqrt((bonus_x - x) * (bonus_x - x) + (y - bonus_y) * (y - bonus_y) // 28))
   l_23 = (l_23[-1] // GRÖßE) + 1

 if x >= bonus_x and y >= bonus_y:
  if (y - bonus_y) == (x - bonus_x):
   l_24.append(math.sqrt((x - bonus_x) * (x - bonus_x) + (y - bonus_y) * (y - bonus_y) // 28))
   l_24 = (l_24[-1] // GRÖßE) + 1


 print(l_23)







 ki_steuerung = lernen(l_1, l_2, l_3, l_4, l_5, l_6, l_7, l_8, l_9, l_10, l_12, l_13, l_14, l_15, l_16)
 return ki_steuerung
