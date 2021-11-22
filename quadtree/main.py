import random

import pygame
from pygame.math import Vector2

import core
from point2d import Point2d
from quadtree import QuadTree
from rectangle import Rectangle


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 800]
    core.memory("capacity",4)
    core.memory("quadtree",QuadTree(Rectangle(0,0,core.WINDOW_SIZE[0],core.WINDOW_SIZE[1]),core.memory("capacity")))

    for i in range(0, 5):
        core.memory("quadtree").insert(Point2d(random.randint(0, core.WINDOW_SIZE[0]),random.randint(0, core.WINDOW_SIZE[1])))



    print("Setup END-----------")


def run():
    core.cleanScreen()
    if core.getKeyPressList(pygame.K_r):
        reset()
    core.memory("quadtree").show(core.screen)
    if core.getMouseLeftClick():
        print(core.getMouseLeftClick())
        core.memory("quadtree").insert(Point2d(core.getMouseLeftClick()[0],core.getMouseLeftClick()[1]))

def reset():
    core.memory("quadtree",
                QuadTree(Rectangle(0, 0, core.WINDOW_SIZE[0], core.WINDOW_SIZE[1]), core.memory("capacity")))
core.main(setup, run)
