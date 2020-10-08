#Auteur LOLA C.
from pygame import Vector2
import core
import random
import pygame
from math import sqrt


balls = []

player= []

creeps=[]

r=10



def setup() :
    print("Setup START---------")
    global balls, player, creeps, r
    core.WINDOW_SIZE = [800, 4800]


    player = player + [200,200,0,0,(255,0,0),r]

    for i in range(0, 1):
        balls = balls + [[random.randint(r,800-r),random.randint(r,800-r),random.uniform(-1,1),random.uniform(-1,1),(random.uniform(0,255),random.uniform(0,255),random.uniform(0,255)),r]]

    for i in range(0,100):
        creeps = creeps + [[random.randint(r, 800 - r), random.randint(r, 800 - r),(random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255)), 5]]

    print("Setup END-----------")

def run() :
    global balls, player, creeps
    if core.getMouseLeftClick() is not None:

        print(core.getMouseLeftClick())
        dir= spring(player,core.getMouseLeftClick(),-1,10)

        player[0]= int(player[0]+dir[0]/10)
        player[1]= int(player[1]+dir[1]/10)

        for b in balls:
            dir= spring(player,b,2,1)
            b[0]=int(b[0]+dir[0]/10)
            b[1] = int(b[1] + dir[1] / 10)



    pygame.draw.circle(core.screen, player[4], (player[0],player[1]),player[5])


    for c in creeps:
        pygame.draw.circle(core.screen, c[2], (c[0], c[1]), c[3])

    for c in creeps:
        e=eatCreep(player,c)
        if e==True:
            player[5]=player[5]+1
            c[0]=(random.randint(r, 800 - r))
            c[1]=(random.randint(r, 800 - r))
            c[2]=(random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255))

def spring(balls1, balle2, k, L0):
    dir = Vector2(balle2[0] - balls1[0], balle2[1] - balls1[1])
    if dir[0] == 0 and dir[1] == 1:
        return [0, 0]
    dirNormalized = dir.normalize()
    Fx = dirNormalized[0] * -k * abs(dir.length() - L0)
    Fy = dirNormalized[1] * -k * abs(dir.length() - L0)
    return [Fx, Fy]


def eatCreep(p,c):
    dist=sqrt(((p[0]-c[0])**2)+((p[1]-c[1])**2))
    if dist<=p[5]+c[3]:
        return True
    else:
        return False

core.main(setup, run)

