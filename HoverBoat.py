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

class Backgrounds:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image_opening = pygame.image.load(join('images','opening.png')).convert_alpha()
        self.opening = pygame.transform.scale(self.image_opening,(SIZE))
        self.image_water = pygame.image.load(join('images','water.png')).convert_alpha()
        self.water = pygame.transform.scale(self.image_water,(SIZE))
        self.gameover = pygame.image.load(join('images','gameover.png')).convert_alpha()

BG = Backgrounds(0,0)
HB = sprites.Hoverboat(-10,210,50,50)
ROCKS = [
    sprites.Rock(   50,  0, 50, 50,-1), 
    sprites.Rock( -350, 50, 50, 50, 2), 
    sprites.Rock(  850, 40, 50, 50,-1), 
    sprites.Rock(  950,100, 50, 50,-2), 
    sprites.Rock( -200,200, 50, 50, 1) 
    ]

splashscreen = True
gameover = False

def redrawGameWindow():
    window.fill((0,60,250))
    if BG.x < SCREENWIDTH:
        BG.x +=1
        if BG.x >= SCREENWIDTH:
            BG.x = 0
    window.blit(BG.water,(BG.x,BG.y))
    window.blit(BG.water,(BG.x+SCREENWIDTH,BG.y))
    window.blit(BG.water,(BG.x-SCREENWIDTH,BG.y))
    window.blit(BG.water,(BG.x,BG.y+SCREENHEIGHT))
    window.blit(BG.water,(BG.x,BG.y-SCREENHEIGHT))
    
    
    HB.draw(window)

    for ROCK in ROCKS:
        ROCK.draw(window)

    if (splashscreen):
        window.blit(BG.opening,(0,0))

    if (gameover):
        window.blit(BG.gameover,(SCREENWIDTH//2-150,SCREENHEIGHT//2-105))

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
        if (HB.thrust == HB.max_vel):
            HB.thrust = 0
        else: HB.thrust += 1
        HB.down = False
        HB.left = False
        HB.right = False
    elif keys[pygame.K_DOWN]:
        splashscreen = False
        HB.up = False
        HB.down = True
        HB.left = False
        HB.right = False
        if (pygame.KEYUP):
            if (gameover):
                gameover = False
            else:
                gameover = True
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
    
    # collision check
    for ROCK in ROCKS:
        if HB.hitbox[0] == ROCK.hitbox[0]:
            print('hit')
    

    redrawGameWindow()

pygame.quit()
    