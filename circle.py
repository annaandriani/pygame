
# coding: iso-8859-1 -*- 

from random import random
from random import *
from turtle import circle
import pygame
from sys import exit
from pygame.locals import *



pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((639,470),0,32)
screen.lock()
for i in range(25):
    random_color = (randint(0,255), randint(0,255), randint(0,255))
    random_pos = (randint(0,639), randint(0,479))
    random_radius = randint(1,200)
    pygame.draw.circle(screen,random_color,random_pos, random_radius)
screen.unlock()

pygame.display.update()

while True:
    for event in pygame.event.get():
         if event.type == QUIT:
             pygame.quit()
             exit()

pygame.quit()
exit()