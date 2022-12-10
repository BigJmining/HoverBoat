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


HB = sprites.Hoverboat(-10,210,50,50)
splashscreen = True
def redrawGameWindow():
    window.fill((0,60,250))
    if (splashscreen):
        window.blit(opening_splashscreen,(0,0))

    HB.draw(window)

    pygame.display.update()

run = True
while run:
    clock.tick(FPS)
    
    # key checks
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        splashscreen = False
        HB.up = True
        # if pygame.KEYUP:
        if (HB.thrust):
            HB.thrust = 0
        else: HB.thrust = 1
        HB.down = False
        HB.left = False
        HB.right = False
    elif keys[pygame.K_DOWN]:
        splashscreen = False
        HB.up = False
        HB.down = True
        HB.left = False
        HB.right = False
    elif keys[pygame.K_LEFT]:
        splashscreen = False
        HB.angle += 5
        HB.up = False
        HB.down = False
        HB.left = True
        HB.right = False
    elif keys[pygame.K_RIGHT]:
        splashscreen = False
        HB.angle += -5
        HB.up = False
        HB.down = False
        HB.left = False
        HB.right = True

    elif keys[pygame.K_q]:
        run = False
    # closing function
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    redrawGameWindow()

pygame.quit()
    