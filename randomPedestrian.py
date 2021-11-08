import random
import pygame
from pygame.math import Vector2
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
    core.memory("Pos",[200,200])
    core.memory("Prev", [200, 200])

    print("Setup END-----------")


def run():
    core.printMemory()
    x = core.memory("Pos")[0] + random.randint(-10,10)
    y = core.memory("Pos")[1] + random.randint(-10,10)


    core.memory("Pos", [x, y])

    pygame.draw.line(core.screen,(255,255,255),core.memory("Pos"),core.memory("Prev"),2)
    core.memory("Prev", [x, y])

core.main(setup, run)
