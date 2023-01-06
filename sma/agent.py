import random

from pygame import Vector2

import core
from sma.body import Body
from sma.creep import Creep
from sma.obstacle import Obstacle


class Agent:
    def __init__(self):
        self.body = Body()
        self.listePerception = []
        self.uuid = random.randint(0, 99999999999999)


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
        voisin, target, obstacles = self.filtre()
        rep = Vector2(0, 0)
        if target is None:
            att = Vector2(0, 0)
        else:
            att = target.position - self.body.position
        for v in voisin:
            if v.taille != 0:
                if v.taille > self.body.taille:
                    rep += self.body.position - v.position
                else:
                    att += v.position - self.body.position
        for o in obstacles:
            rep += (self.body.position - o.position)
        if len(voisin) != 0:
            rep /= len(voisin)
        return rep + att

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

