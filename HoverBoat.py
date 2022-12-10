#!/usr/bin/env python3
# by Jason Lohrey

''' 
HOVERBOAT is a 2d top-down boat game where players avoid
rocks and the shore, while shooting fish for points.

Based off the classic Astriod game engine (all hail Astroid)
and ship movement
'''

# import libraries needed
import pygame
from os.path import join

import sprites 

pygame.init()

SIZE = SCREENWIDTH,SCREENHEIGHT= 600,300
FPS = 60

window = pygame.display.set_mode((SIZE))
pygame.display.set_caption("HOVERBOAT 2052")
clock = pygame.time.Clock()

opening_splashscreen = pygame.image.load(join('images','opening.png'))


HB = sprites.Hoverboat(-100,210,50,50)

def redrawGameWindow():
    window.blit(opening_splashscreen,(0,0))

    HB.draw(window)

    pygame.display.update()

run = True
while run:
    clock.tick(FPS)
    
    # key checks

    # closing function
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    redrawGameWindow()

pygame.quit()
    