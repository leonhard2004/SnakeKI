import pygame as pg, random as rnd
from snake_learn import lernen     #gibt infos am ende des Programms an den Kopf der KI.
screen = pg.display.set_mode([1000, 600])
import math

def diagonaler_abstand(abstand_1, abstand_2):
 diagonale = abstand_1, abstand_2      #abstand_1 und abstand_2 werden auf die kleinere Zahl wird reduziert, die dann auch der Diagonale entspricht.
 sortierte_diagonale = sorted(diagonale)
 layer = sortierte_diagonale[0]
 return layer

def layer_apple(bonus_a, bonus_b, a, b, SIZE):
 if bonus_a == a and bonus_b > b:
  layer = (bonus_b - b) / SIZE          #l_17-20 werden hier durch unterschiedliche Reihenfolgen der Variablen ausgerechnet.
 else:
  layer = 0
 return layer

def all_layers(richt_x, richt_y, score, tempo, snake, bonus_x, bonus_y, SIZE, WIDTH, HEIGHT, x, y):
#ersten 4 Wand_Layer durch simples ausrechnen:
 l_1 = y / SIZE                 #Abstand zur Wand wird einfach durch 20 geteilt, um auf die richtige Höhe zu kommen.
 l_2 = (WIDTH - x) / SIZE
 l_3 = (HEIGHT - y) / SIZE      #Abstand wird ausgerechnet und durch 20 geteilt.
 l_4 = x / SIZE

#zweiten 4 Wand_Layer:
 l_5 = diagonaler_abstand(l_1, l_2)
 l_6 = diagonaler_abstand(l_2, l_3)
 l_7 = diagonaler_abstand(l_3, l_4)
 l_8 = diagonaler_abstand(l_4, l_1)

#Variablen, die für die weiteren Layer wichtig sind:
 kopf = snake[-1]
 kopf_x = kopf[0]
 kopf_y = kopf[1]

#Layer 9 - 16 werden definiert:
 l_9 = [0]
 l_10 = [0]
 l_11 = [0]
 l_12 = [0]
 l_13 = [0]
 l_14 = [0]
 l_15 = [0]
 l_16 = [0]

#Layer_9:
 for (x,y) in snake:                #for Schleife, um alle Körperteile von der Snake durchzurechnen.
  if x == kopf_x and y <= kopf_y:
   l_9.append((kopf_y - y) / SIZE)  #.append, um an die schon bestehende Liste anzuhängen, und sie nicht komplett zu überschreiben.
 l_9 = float(l_9[-2])               #[-2], um den vorletzten Eintrag der Lista zu nehmen, und "float", um immer eine Ganzzahl zu erhalten.

#Layer_10:
 for (x,y) in snake:
  if y == kopf_y and x <= kopf_x:
   l_10.append((kopf_x - x) / SIZE)
 l_10 = float(l_10[-2])

#Layer_11:
 for (x,y) in snake:
  if x == kopf_x and kopf_y <= y:
   l_11.append((y - kopf_y) / SIZE)
 l_11 = float(l_11[-2])

#Layer_12:
 for (x,y) in snake:
  if y == kopf_y and kopf_x <= x:
   l_12.append((x - kopf_x) / SIZE)
 l_12 = float(l_12[-2])

#Layer_13(diagonal):
 for (x,y) in snake:
  if x >= kopf_x and y <= kopf_y:
   if (kopf_y - y) == (x - kopf_x):     #Man braucht den "Satz des Pytagoras".
    l_13.append(math.sqrt(((((x - kopf_x) * (x - kopf_x) + (kopf_y - y) * (kopf_y - y))) / SIZE) ** 2) // SIZE)
 l_13 = float(l_13[-2])

#Layer_14(diagonal):
 for (x,y) in snake:
  if x >= kopf_x and y >= kopf_y:
   if (y - kopf_y) == (x - kopf_x):
    l_14.append(math.sqrt(((((x - kopf_x) * (x - kopf_x) + (y - kopf_y) * (y - kopf_y))) / SIZE) ** 2) // SIZE)
 l_14 = float(l_14[-2])

#Layer_15(diagonal):
 for (x,y) in snake:
  if x <= kopf_x and y >= kopf_y:
   if (y - kopf_y) == (kopf_x - x):
    l_15.append(math.sqrt(((((kopf_x - x) * (kopf_x - x) + (y - kopf_y) * (y - kopf_y))) / SIZE) ** 2) // SIZE)
 l_15 = float(l_15[-2])

#Layer_16(diagonal):
 for (x,y) in snake:
  if x <= kopf_x and y <= kopf_y:
   if (kopf_y - y) == (kopf_x - x):
    l_16.append(math.sqrt(((((kopf_x - x) * (kopf_x - x) + (kopf_y - y) * (kopf_y - y))) / SIZE) ** 2) // SIZE)
 l_16 = float(l_16[-2])

#Layer 17 - 19 durch tauschen der Variablen für die Definition:
 l_17 = layer_apple(bonus_x, bonus_y, kopf_x, kopf_y, SIZE)
 l_18 = layer_apple(bonus_y, x, y, bonus_x, SIZE)
 l_19 = layer_apple(bonus_x, y, x, bonus_y, SIZE)
 l_20 = layer_apple(bonus_y, bonus_x, y, x, SIZE)

#Layer 21 - 24 werden definiert:
 l_21 = [0]
 l_22 = [0]
 l_23 = [0]
 l_24 = [0]

#Layer_21:
 if bonus_x >= kopf_x and bonus_y <= kopf_y:
  if (kopf_y - bonus_y) == (bonus_x - kopf_x):          #"Satz des Pytagoras", kann durch den import von math ausgerechnet werden(die Wurzel kann gezogen werden).
   l_21.append(math.sqrt((kopf_x - bonus_x) * (kopf_x - bonus_x) + (bonus_y - kopf_y) * (bonus_y - kopf_y) // 28))
 l_21 = float(l_21[-1] // SIZE)                         #Soll immer in einem float angegeben werden.

#Layer_22:
 if kopf_x <= bonus_x and kopf_y <= bonus_y:
  if (bonus_y - kopf_y) == (bonus_x - kopf_x):
   l_22.append(math.sqrt((bonus_x - kopf_x) * (bonus_x - kopf_x) + (bonus_y - kopf_y) * (bonus_y - kopf_y) // 28))
 l_22 = float(l_22[-1] // SIZE)

#Layer_23:
 if bonus_x <= kopf_x and bonus_y >= kopf_y:
  if (bonus_y - kopf_y) == (kopf_x - bonus_x):
   l_23.append(math.sqrt((bonus_x - kopf_x) * (bonus_x - kopf_x) + (kopf_y - bonus_y) * (kopf_y - bonus_y) // 28))
 l_23 = float(l_23[-1] // SIZE)

#Layer_24:
 if kopf_x >= bonus_x and kopf_y >= bonus_y:
  if (kopf_y - bonus_y) == (kopf_x - bonus_x):
   l_24.append(math.sqrt((kopf_x - bonus_x) * (kopf_x - bonus_x) + (kopf_y - bonus_y) * (kopf_y - bonus_y) // 28))
 l_24 = float(l_24[-1] // SIZE)

 ki_steuerung = lernen(l_1, l_2, l_3, l_4, l_5, l_6, l_7, l_8, l_9, l_10, l_12, l_13, l_14, l_15, l_16, l_17, l_18, l_19, l_20, l_21, l_22, l_23, l_24, score)
 return ki_steuerung        #gibt alle Layer an den Kopf der KI in nimmt das Ergebnis in einer Variable an und gibt es direckt zurück zu dem Hauptspiel.
