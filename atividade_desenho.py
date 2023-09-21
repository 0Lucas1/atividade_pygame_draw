import pygame as pg
from pygame.locals import *
from random import randint

tela = pg.display.set_mode((500,450))

pg.display.set_caption('Desenhar')

cond_r,cond_q,cond_c = 0,0,0

tela.fill((255,255,255))

while True:
    teclas = pg.key.get_pressed()
    for evento in pg.event.get():
        if evento.type == QUIT:
            pg.quit()
        if evento.type == MOUSEBUTTONDOWN:
            x,y = evento.pos
            if cond_r:
                pg.draw.rect(tela,(255,0,0),(x,y,30,100))
            elif cond_c:
                pg.draw.circle(tela,(0,255,0),(x,y),10)
            elif cond_q:
                pg.draw.rect(tela,(0,0,255),(x,y,30,30))
            else:
                pg.draw.rect(tela,(randint(0,255),randint(0,255),randint(0,255)),(x,y,50,70))
    teclas = pg.key.get_pressed()
    if teclas[K_q]:
        cond_q = 1
        cond_c,cond_r  = 0,0
    if teclas[K_r]:
        cond_r = 1
        cond_c,cond_q  = 0,0
    if teclas[K_c]:
        cond_c = 1
        cond_q,cond_r  = 0,0
    if teclas[K_l]:
      cond_r,cond_q,cond_c = 0,0,0
      tela.fill((255,255,255))
    pg.display.update()