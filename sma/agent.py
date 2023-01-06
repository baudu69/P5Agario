import random

from pygame import Vector2

import core
from sma.body import Body
from sma.creep import Creep
from sma.etat import Etat
from sma.obstacle import Obstacle


class Agent:
    def __init__(self, etat=Etat.SAIN):
        self.body = Body(self)
        self.listePerception = []
        self.uuid = random.randint(0, 99999999999999)
        self.etat = etat


    def filtre(self):
        centre = None
        voisin = []
        obstacles = []
        for p in self.listePerception:
            if isinstance(p, Creep):
                centre = p
            elif isinstance(p, Obstacle):
                obstacles.append(p)
            else:
                voisin.append(p)
        return voisin, centre, obstacles

    def update(self):
        return Vector2(random.randint(-10, 10), random.randint(-10, 10))

    def show(self):
        self.body.show()

    def computePerception(self):
        self.body.fustrum.objetsPercus = []
        for agent in core.memory("agents"):
            if not agent.uuid == self.uuid:
                if self.body.fustrum.inside(agent.body):
                    self.listePerception.append(agent.body)
        for creep in core.memory("creeps"):
            if (self.body.fustrum.insideObject(creep)):
                self.body.taille += 0.5
                creep.reset()
            if self.body.fustrum.inside(creep):
                self.listePerception.append(creep)

        for agent in core.memory("agents"):
            if not agent.uuid == self.uuid:
                if self.body.fustrum.insideObject(agent.body):
                    self.body.taille += 0.2*agent.body.taille
                    self.body.fustrum.majRadius()
                    agent.body.taille = 0

        for obstacle in core.memory("obstacles"):
            if self.body.fustrum.inside(obstacle):
                self.listePerception.append(obstacle)

    def compteDecision(self):
        self.body.move(self.update())

