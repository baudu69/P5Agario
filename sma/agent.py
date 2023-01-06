import random

from pygame import Vector2

import core
from sma.body import Body
from sma.creep import Creep
from sma.etat import Etat
from sma.obstacle import Obstacle


class Agent:
    def __init__(self, etat=Etat.SAIN, groupe=0):
        self.body = Body(self)
        self.listePerception = []
        self.uuid = random.randint(0, 99999999999999)
        self.etat = etat
        self.groupe = groupe


    def filtre(self):
        fratrie = []
        for p in self.listePerception:
            if self.groupe == p.groupe:
                fratrie.append(p)
        return fratrie

    def update(self):
        self.body.update()
        att = Vector2(0, 0)
        rep = Vector2(0, 0)
        fratrie = self.filtre()
        for frere in fratrie:
            if self.etat == Etat.MALADE:
                rep += self.body.position - frere.body.position
            else:
                att += frere.body.position - self.body.position
        if len(fratrie) != 0:
            if self.etat == Etat.MALADE:
                rep = rep / len(fratrie)
            else:
                att /= len(fratrie)
        return att + rep + Vector2(random.randint(-10, 10), random.randint(-10, 10))

    def show(self):
        self.body.show()

    def computePerception(self):
        self.body.fustrum.objetsPercus = []
        for agent in core.memory("agents"):
            if not agent.uuid == self.uuid:
                if self.body.fustrum.inside(agent.body):
                    self.listePerception.append(agent)

    def compteDecision(self):
        self.body.move(self.update())

