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

    for i in range(0, 10):
        balls = balls + [[random.randint(0,400),random.randint(0,400),random.uniform(-2,2),random.uniform(-2,2)]]
    print("Setup END-----------")


def run():
    global balls
    for b in balls:
        b[0]= int(b[0]+b[2])
        b[1] = int(b[1] + b[3])

    for b in balls:
        pygame.draw.circle(core.screen, (255, 0, 255), (b[0], b[1]),  10)






core.main(setup, run)
