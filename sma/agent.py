import random

from pygame import Vector2

import core
from sma.body import Body
from sma.etat import Etat


class Agent:
    def __init__(self, etat=Etat.SAIN, groupe=0):
        self.body = Body(self)
        self.listePerception = []
        self.uuid = random.randint(0, 99999999999999)
        self.body.etat = etat
        self.groupe = groupe
        self.etat = Etat.SAIN

    def filtre(self):
        fratrie = []
        maladesRationnels = []
        autres = []
        for p in self.listePerception:
            if p.body.etat == Etat.MALADE_RATIONNEL:
                maladesRationnels.append(p)
            elif self.groupe == p.groupe and p.body.etat != Etat.MORT:
                fratrie.append(p)
            else:
                autres.append(p)

        return fratrie, maladesRationnels, autres

    def update(self):
        self.body.update()
        att = Vector2(0, 0)
        rep = Vector2(0, 0)
        lenrep = 0
        fratrie, maladesRationnels, autres = self.filtre()
        for frere in fratrie:
            if self.body.etat == Etat.MALADE_RATIONNEL:
                rep += self.body.position - frere.body.position
                lenrep += 1
            else:
                att += frere.body.position - self.body.position

        for maladeRationnel in maladesRationnels:
            rep += self.body.position - maladeRationnel.body.position
            lenrep += 1

        if self.body.etat == Etat.MALADE_RATIONNEL:
            for autre in autres:
                rep += self.body.position - autre.body.position
                lenrep += 1

        if len(fratrie) != 0 and self.body.etat != Etat.MALADE_RATIONNEL:
            att /= len(fratrie)

        if lenrep != 0:
            rep /= lenrep
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
