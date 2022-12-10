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
import random

import sprites 

pygame.init()

SIZE = SCREENWIDTH,SCREENHEIGHT= 1200,600
FPS = 60


window = pygame.display.set_mode((SIZE))
pygame.display.set_caption("HOVERBOAT 2052")
clock = pygame.time.Clock()

opening_splashscreen = pygame.image.load(join('images','opening.png'))
water_image = pygame.image.load(join('images','water.png'))
water = pygame.transform.scale(water_image,(SIZE))
opening = pygame.transform.scale(opening_splashscreen,(SIZE))

HB = sprites.Hoverboat(-10,210,50,50)
ROCKS = [
    sprites.Rock(   50,  0, 50, 50), 
    sprites.Rock( -350, 50, 50, 50), 
    sprites.Rock( -650, 40, 50, 50), 
    sprites.Rock( -150,100, 50, 50), 
    sprites.Rock(    0,200, 50, 50) 
    ]

splashscreen = True
def redrawGameWindow():
    window.fill((0,60,250))
    window.blit(water,(0,0))
    
    
    HB.draw(window)

    for ROCK in ROCKS:
        ROCK.draw(window)

    if (splashscreen):
        window.blit(opening,(0,0))

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
        HB.angle += 2
        HB.up = False
        HB.down = False
        HB.left = True
        HB.right = False
    elif keys[pygame.K_RIGHT]:
        splashscreen = False
        HB.angle-= 2
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
    