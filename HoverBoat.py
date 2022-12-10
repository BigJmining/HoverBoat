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

pygame.init()

SIZE = SCREENWIDTH,SCREENHEIGHT= 600,300

window = pygame.display.set_mode((SIZE))
pygame.display.set_caption("HOVERBOAT 2052")

run = True
while run:

    window.fill((0,80,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
    