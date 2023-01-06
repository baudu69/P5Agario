import random

from pygame import Vector2

import core

padding = 100

class Creep:
    def __init__(self):
        self.position = Vector2(random.randint(padding, core.WINDOW_SIZE[0] - padding), random.randint(padding, core.WINDOW_SIZE[1] - padding))
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def show(self):
        core.Draw.circle(self.color, (self.position.x, self.position.y), 2, 0)

    def reset(self):
        self.position = Vector2(random.randint(padding, core.WINDOW_SIZE[0] - padding), random.randint(padding, core.WINDOW_SIZE[1] - padding))
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

