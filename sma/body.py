import random

from pygame import Vector2

import core
from sma.etat import Etat
from sma.fustrom import Fustrom

padding = 40

class Body:
    def __init__(self, parent=None):
        self.position = Vector2(random.randint(padding, core.WINDOW_SIZE[0] - padding),
                                random.randint(padding, core.WINDOW_SIZE[1] - padding))
        self.vitesse = Vector2(random.randint(-10, 10), random.randint(-10, 10))
        self.acceleration = Vector2(random.randint(-10, 10), random.randint(-10, 10))
        self.vMax = 10
        self.accMax = 4
        self.taille = 10
        self.fustrum = Fustrom(self)
        self.parent = parent

    def move(self, decision):
        if decision.length() > self.accMax:
            decision.scale_to_length(self.accMax)
        self.vitesse += decision
        if self.vitesse.length() > self.vMax:
            self.vitesse.scale_to_length(self.vMax)
        self.border()

        self.position += self.vitesse


    def border(self):
        if self.position.x + self.taille >= core.WINDOW_SIZE[0] or self.position.x - self.taille <= 0:
            self.vitesse.x *= -1
            self.acceleration.x *= -1
        if self.position.y + self.taille >= core.WINDOW_SIZE[1] or self.position.y - self.taille <= 0:
            self.vitesse.y *= -1
            self.acceleration.y *= -1

        # If out of border then go to center
        if self.position.x + self.taille >= core.WINDOW_SIZE[0]:
            self.position.x = core.WINDOW_SIZE[0] - self.taille
        if self.position.x - self.taille <= 0:
            self.position.x = self.taille
        if self.position.y + self.taille >= core.WINDOW_SIZE[1]:
            self.position.y = core.WINDOW_SIZE[1] - self.taille
        if self.position.y - self.taille <= 0:
            self.position.y = self.taille

    def show(self):
        if self.parent.etat == Etat.SAIN:
            core.Draw.circle((0, 255, 0), (self.position.x, self.position.y), self.taille, 0)
        elif self.parent.etat == Etat.MALADE:
            core.Draw.circle((255, 0, 0), (self.position.x, self.position.y), self.taille, 0)
        elif self.parent.etat == Etat.IMMUNISE:
            core.Draw.circle((0, 0, 255), (self.position.x, self.position.y), self.taille, 0)
        elif self.parent.etat == Etat.MORT:
            core.Draw.circle((255, 255, 255), (self.position.x, self.position.y), self.taille, 0)
