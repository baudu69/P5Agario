import random
import pygame
from pygame.math import Vector2
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]

    core.memory("centredecercle", [200, 200])
    core.memory("rayonducercle", 100)
    core.memory("couleurducercle", (255, 0, 0))

    print("Setup END-----------")


def run():
    pygame.draw.circle(core.screen, core.memory("couleurducercle"), core.memory("centredecercle"), core.memory("rayonducercle"))
    print(core.getMouseLeftClick())

core.main(setup, run)
