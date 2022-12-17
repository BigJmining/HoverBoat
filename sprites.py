import pygame
from os.path import join
import math


SIZE = SCREENWIDTH,SCREENHEIGHT= 1200,600

class Hoverboat:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x + 17, self.y +11, 32, 55)
        self.right = False
        self.left = False
        self.up = True
        self.down = False
        self.angle = 0
        self.angle_change = 0
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
        self.sunk = pygame.image.load(join('images','hoverboat_up_SUNK.png'))
        self.rect = self.image_up.get_rect()
        self.speed = 0

    def addVectors(angle1, length1, angle2, length2):
        x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
        y  = math.cos(angle1) * length1 + math.cos(angle2) * length2
        
        angle = 0.5 * math.pi - math.atan2(y, x)
        length  = math.hypot(x, y)

        return (angle, length)

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
        

        image = self.image_up
        rotated_image = pygame.transform.rotate(image,+float(self.angle))
        window.blit(rotated_image,(self.x,self.y))

        self.hitbox = (self.x + 5, self.y +0, 80, 80)
        pygame.draw.rect(window,(255,0,0),self.hitbox,2)
        

        
class Rock:
    def __init__(self,x,y,width,height,direction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x + 5, self.y +0, 80, 80)
        self.vel_x = direction
        self.vel_y = direction
        self.max_vel = 2
        self.thrust = 1
        self.angle = 0
        self.image = pygame.image.load(join('images','rock.png'))

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
        image = self.image

        rotated_image = pygame.transform.rotate(image,+float(self.angle))
        window.blit(rotated_image,(self.x,self.y))

        self.hitbox = (self.x + 5, self.y +0, 80, 80)
        pygame.draw.rect(window,(255,0,0),self.hitbox,2)