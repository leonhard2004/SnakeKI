from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
import pygame as pg, random as rnd
from snake_KI import all_layers

def spielstart():
 WIDTH, HEIGHT = 1000, 600
 SIZE = 20
 score, tempo = 0, 5
 snake = [(WIDTH//2, HEIGHT//2)]
 richt_x, richt_y = 1, 0
 bonus_x, bonus_y = 300, 300
 richtungen = {pg.K_s: (0,1), pg.K_DOWN: (0,1), pg.K_w: (0,-1), pg.K_UP: (0,-1), pg.K_a: (-1,0),
 pg.K_LEFT: (-1,0), pg.K_d: (1,0), pg.K_RIGHT: (1,0)}

 pg.init()
 screen = pg.display.set_mode([WIDTH, HEIGHT])

 weitermachen = True
 clock = pg.time.Clock()

 while weitermachen:
  clock.tick(tempo)
  screen.fill((0,0,0))

  for ereignis in pg.event.get():
   if ereignis.type == pg.QUIT:
    weitermachen = False
   if ereignis.type == pg.KEYDOWN and ereignis.key in richtungen:
    richt_x, richt_y = richtungen[ereignis.key]

  x,y = snake[-1]
  ki_steuerung = all_layers(richt_x, richt_y, score, tempo, snake, bonus_x, bonus_y, SIZE, WIDTH, HEIGHT, x, y)


  x,y = x + richt_x * SIZE, y + richt_y * SIZE
  if x < 0 or x + SIZE > WIDTH or y < 0 or y + SIZE > HEIGHT or (x,y) in snake:
   weitermachen = False
  snake.append((x,y))

  if x == bonus_x and y == bonus_y:
   score += tempo + 10
   tempo += 1
   bonus_x = rnd.randrange(WIDTH) // SIZE * SIZE
   bonus_y = rnd.randrange(HEIGHT) // SIZE * SIZE
  else:
   del snake[0]



  for x,y in snake:
   pg.draw.rect(screen,(0,255,0),(x,y,SIZE, SIZE))
   pg.draw.rect(screen,(255,0,0),(bonus_x,bonus_y,SIZE, SIZE))

  textfläche = pg.font.SysFont('impact', 28).render(f'Score: {score}', False, (255,255,255))
  screen.blit(textfläche, (WIDTH - textfläche.get_width(), 5))
  pg.display.flip()

spielstart()
