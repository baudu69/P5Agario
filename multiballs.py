
import random
import pygame
from pygame.math import Vector2
import core

balls = []


def setup():
    global balls
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
    rMax=10
    nbBalls = int(input("Nombre de balles ?"))
    for i in range(0, nbBalls):
        balls = balls + [[random.randint(rMax,400-rMax),random.randint(rMax,400-rMax),random.uniform(-5,5),random.uniform(-5,5),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),random.randint(10,rMax)]]
        print(balls)
    print("Setup END-----------")


def run():
    global balls


    #Rebond
    for b in balls:
        print(b)
        if b[0] > core.WINDOW_SIZE[0]-b[5]:
            b[2] = abs(b[2]) * -1
            b[4] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if b[0] < b[5] :
            b[2] = abs(b[2])
            b[4]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            print("change X")

        if b[1] > core.WINDOW_SIZE[1]-b[5] :
            b[3] = abs(b[3]) * -1
            b[4] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            print("change Y")
        if  b[1] < b[5]:
            b[3] = abs(b[3])
    
    for b in balls:
        b[0]= int(b[0]+ 5*b[2])
        b[1] = int(b[1] + 5*b[3])

    for b in balls:
        pygame.draw.circle(core.screen, (b[4]), (b[0], b[1]),  b[5])




core.main(setup, run)
