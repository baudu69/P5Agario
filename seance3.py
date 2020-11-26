import random
import pygame
import core

ball1= []
ball2= []


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]

    global ball1,ball2
    ball1= [200,200,0,0,255,0,0]
    ball2 =[random.randint(0,400),random.randint(0,400),0,0,0,0,255]

    print("Setup END-----------")

def Spring(b1,b2,k,lo):
    u = pygame.Vector2(b2[0] - b1[0], b2[1] - b1[1])
    distanceEntreB1etB2 = u.length()

    if u[0] == 0 and u[1]==0:
        return [0,0]

    u = u.normalize()

    Fx = u[0] * k * abs(distanceEntreB1etB2  - lo)
    Fy = u[1] * k * abs(distanceEntreB1etB2  - lo)

    return [Fx,Fy]

def run():
    print("running")
    pygame.draw.circle(core.screen,(ball1[4],ball1[5],ball1[6]),(ball1[0],ball1[1]),40)

    pygame.draw.circle(core.screen, (ball2[4], ball2[5], ball2[6]),  (ball2[0], ball2[1]), 40)

    Frappel = Spring(ball1,ball2,-0.5,20)

    ball2[0]=int(ball2[0]+Frappel[0])
    ball2[1]=int(ball2[1]+Frappel[1])

    if core.getMouseLeftClick() is not None:
        FrappelSouris = Spring(core.getMouseLeftClick(),ball1,-1,10)
        ball1[0]=int(ball1[0]+FrappelSouris[0])
        ball1[1]=int(ball1[1]+FrappelSouris[1])


core.main(setup, run)
