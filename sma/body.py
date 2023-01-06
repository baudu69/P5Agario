import random

from pygame import Vector2

import core
from sma.epidemie import Epidemie
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
        self.delai = 30*10
        self.etat = Etat.SAIN

    def move(self, decision):
        if decision.length() > self.accMax:
            decision.scale_to_length(self.accMax)
        self.vitesse += decision
        if self.vitesse.length() > self.vMax:
            self.vitesse.scale_to_length(self.vMax)
        self.border()
        if self.etat == Etat.MORT:
            self.vitesse = Vector2(0, 0)

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

    def update(self):
        if self.etat == Etat.INCUBATION and self.delai == 0:
            self.etat = Etat.CONTAGIEUX
            self.delai = Epidemie.dureeContagion.value
        elif self.etat == Etat.CONTAGIEUX and self.delai == 0:
            if random.random() < 0.5:
                self.etat = Etat.MALADE
            else:
                self.etat = Etat.MALADE_RATIONNEL
            self.delai = Epidemie.dureeDeces.value
        elif (self.etat == Etat.MALADE or self.etat == Etat.MALADE_RATIONNEL) and self.delai == 0:
            if random.random() < Epidemie.pourcentageDeces.value:
                self.etat = Etat.MORT
            else:
                self.etat = Etat.IMMUNISE

        if self.etat == Etat.CONTAGIEUX or self.etat == Etat.MALADE:
            chanceContagion = Epidemie.pourcentageContagion.value
            if (self.etat == Etat.MALADE_RATIONNEL):
                chanceContagion *= 0.7
            for agentsAProximite in self.parent.listePerception:
                if agentsAProximite.body.etat == Etat.SAIN and random.random() < chanceContagion:
                    agentsAProximite.body.etat = Etat.INCUBATION
                    agentsAProximite.body.delai = Epidemie.dureeIncubation.value
        self.delai -= 1


    def show(self):
        if self.etat == Etat.SAIN:
            core.Draw.circle((0, 255, 0), (self.position.x, self.position.y), self.taille, 0)
        elif self.etat == Etat.MALADE:
            core.Draw.circle((255, 0, 0), (self.position.x, self.position.y), self.taille, 0)
        elif self.etat == Etat.IMMUNISE:
            core.Draw.circle((0, 0, 255), (self.position.x, self.position.y), self.taille, 0)
        elif self.etat == Etat.MORT:
            core.Draw.circle((255, 255, 255), (self.position.x, self.position.y), self.taille, 0)
        elif self.etat == Etat.INCUBATION:
            core.Draw.circle((255, 255, 0), (self.position.x, self.position.y), self.taille, 0)
        elif self.etat == Etat.CONTAGIEUX:
            core.Draw.circle((255, 0, 255), (self.position.x, self.position.y), self.taille, 0)
        elif self.etat == Etat.MALADE_RATIONNEL:
            core.Draw.circle((255, 140, 0), (self.position.x, self.position.y), self.taille, 0)
