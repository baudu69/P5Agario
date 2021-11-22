import pygame


class Point2d:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def show(self,screen):
        pygame.draw.circle(screen,(255,0,0),(self.x,self.y),2)