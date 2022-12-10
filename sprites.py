import pygame
from os.path import join

SIZE = SCREENWIDTH,SCREENHEIGHT= 600,300


class Hoverboat:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.right = False
        self.left = False
        self.up = True
        self.down = False
        self.angle = 0
        self.thrust = 0
        self.vel_x = 1
        self.vel_y = 1
        self.max_vel = 3
        self.image_up = pygame.image.load(join('images','hoverboat_up_still.png'))
        self.image_up_thrust = pygame.image.load(join('images','hoverboat_up_thrust.png'))
        self.image_down = pygame.transform.flip(self.image_up,0,1)
        self.image_down_thrust = pygame.transform.flip(self.image_up_thrust,0,1)
        self.image_right = pygame.transform.rotate(self.image_up,-90)
        self.image_right_thrust = pygame.transform.rotate(self.image_up_thrust,-90)
        self.image_left = pygame.transform.flip(self.image_right,1,0)
        self.image_left_thrust = pygame.transform.flip(self.image_right_thrust,1,0)

    def move(self):
        if self.vel_x > 0:
            if self.x + self.thrust < SCREENWIDTH - self.width:
                self.x += self.thrust * self.vel_x
                # print('l-r ',self.x,'-',self.vel_x)
                if self.x +self.thrust >= SCREENWIDTH-self.width:
                    if self.vel_x < self.max_vel:
                        self.vel_x += 0.5
                    elif self.vel_x == self.max_vel:
                        self.vel_x = self.thrust
                    self.vel_x = self.vel_x * -1
        if self.vel_x < 0:
            if self.x - self.thrust > 0-self.width:
                self.x += self.thrust * self.vel_x
                # print('r-l ',self.x,'-',self.vel_x)
                if self.x - self.thrust <= 0 - self.width:
                    self.vel_x = self.vel_x * -1

        if self.vel_y > 0:
            if self.y + self.thrust < SCREENHEIGHT - self.height:
                self.y += self.thrust * self.vel_y
                # print('l-r ',self.y,'-',self.vel_y)
                if self.y +self.thrust >= SCREENHEIGHT-self.height:
                    if self.vel_y < self.max_vel:
                        self.vel_y += 0.5
                    elif self.vel_y == self.max_vel:
                        self.vel_y = 1
                    self.vel_y = self.vel_y * -1
        if self.vel_y < 0:
            if self.y - self.thrust > 0-self.height:
                self.y += self.thrust * self.vel_y
                # print('r-l ',self.y,'-',self.vel_y)
                if self.y - self.thrust <= 0 - self.height:
                    self.vel_y = self.vel_y * -1

    def draw(self,window):
        self.move()
        if (self.up):
            window.blit(self.image_up,(self.x,self.y))
            if (self.thrust):
                window.blit(self.image_up_thrust,(self.x,self.y))
        if (self.down):
            window.blit(self.image_down,(self.x,self.y))
            if (self.thrust):
                window.blit(self.image_down_thrust,(self.x,self.y))
        if (self.right):
            window.blit(self.image_right,(self.x,self.y))
            if (self.thrust):
                window.blit(self.image_right_thrust,(self.x,self.y))
        if (self.left):
            window.blit(self.image_left,(self.x,self.y))
            if (self.thrust):
                window.blit(self.image_left_thrust,(self.x,self.y))
        
