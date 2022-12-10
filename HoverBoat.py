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

pygame.init()

SIZE = SCREENWIDTH,SCREENHEIGHT= 600,300
FPS = 60

window = pygame.display.set_mode((SIZE))
pygame.display.set_caption("HOVERBOAT 2052")
clock = pygame.time.Clock()

opening_splashscreen = pygame.image.load(join('images','opening.png'))

class Hoverboat:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 1
        self.image = pygame.image.load(join('images','hoverboat_up_still.png'))

    def move(self):
        if self.x + 1 < SCREENWIDTH:
            if self.x > SCREENWIDTH:
                self.vel *= -1
            self.x += 1 * self.vel
        if self.x <= 0:
            self.vel *= -1


    def draw(self,window):
        self.move()
        window.blit(self.image,(self.x,self.y))


HB = Hoverboat(0,210,50,50)

run = True
while run:
    clock.tick(FPS)
    window.fill((0,80,255))
    window.blit(opening_splashscreen,(0,0))
    
    HB.draw(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
    