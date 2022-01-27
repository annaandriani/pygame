# coding: iso-8859-1 -*- 

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
pygame.font.init()


screen = pygame.display.set_mode((639,470))
pygame.display.set_caption("Teste cores")

white = (255,250,250)
blue = (135,206,250)
pink = (255,20,147)

game_exit = False
while not game_exit:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_exit= True
    screen.fill(pink)
while True:
    for event in pygame.event.get():
         if event.type == QUIT:
             pygame.quit()
             exit()
            
    screen.fill(blue)

    mouse_pos = pygame.mouse.get_pos()
    for x in range(0,640,20):
        pygame.draw.line(screen,(0,0,0),(x,0),mouse_pos)
        pygame.draw.line(screen,(0,0,0),(x,470),mouse_pos)

    for y in range(0,480,20):
        pygame.draw.line(screen,(0,0,0),(0,y),mouse_pos)
        pygame.draw.line(screen,(0,0,0),(639,y),mouse_pos)

    pygame.display.update()

pygame.quit()
exit()