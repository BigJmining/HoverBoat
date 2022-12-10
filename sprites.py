import pygame
from os.path import join

SIZE = SCREENWIDTH,SCREENHEIGHT= 600,300


class Hoverboat:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel_x = 1
        self.vel_y = 1
        self.max_vel = 6
        self.image = pygame.image.load(join('images','hoverboat_up_still.png'))

    def move(self):
        if self.vel_x > 0:
            if self.x + 1 < SCREENWIDTH - self.width:
                self.x += 1 * self.vel_x
                # print('l-r ',self.x,'-',self.vel_x)
                if self.x +1 >= SCREENWIDTH-self.width:
                    if self.vel_x < self.max_vel:
                        self.vel_x += 0.5
                    elif self.vel_x == self.max_vel:
                        self.vel_x = 1
                    self.vel_x = self.vel_x * -1
        if self.vel_x < 0:
            if self.x - 1 > 0-self.width:
                self.x += 1 * self.vel_x
                # print('r-l ',self.x,'-',self.vel_x)
                if self.x - 1 <= 0 - self.width:
                    self.vel_x = self.vel_x * -1

        if self.vel_y > 0:
            if self.y + 1 < SCREENHEIGHT - self.height:
                self.y += 1 * self.vel_y
                # print('l-r ',self.y,'-',self.vel_y)
                if self.y +1 >= SCREENHEIGHT-self.height:
                    if self.vel_y < self.max_vel:
                        self.vel_y += 0.5
                    elif self.vel_y == self.max_vel:
                        self.vel_y = 1
                    self.vel_y = self.vel_y * -1
        if self.vel_y < 0:
            if self.y - 1 > 0-self.height:
                self.y += 1 * self.vel_y
                # print('r-l ',self.y,'-',self.vel_y)
                if self.y - 1 <= 0 - self.height:
                    self.vel_y = self.vel_y * -1

    def draw(self,window):
        self.move()
        window.blit(self.image,(self.x,self.y))

