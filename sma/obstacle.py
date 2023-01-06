import random

from pygame import Vector2

import core

padding = 100

class Obstacle:
    def __init__(self):
        self.position = Vector2(random.randint(padding, core.WINDOW_SIZE[0] - padding), random.randint(padding, core.WINDOW_SIZE[1] - padding))

    def show(self):
        core.Draw.circle((255, 0, 0), (self.position.x, self.position.y), 20, 0)
