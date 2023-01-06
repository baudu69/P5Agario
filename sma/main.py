from pygame import Vector2

import core
from sma.agent import Agent
from sma.creep import Creep
from sma.epidemie import Epidemie
from sma.etat import Etat
from sma.obstacle import Obstacle

nbAgents = 7
nbGroupes = 3
nbCreeps = 0
nbObstacles = 0


def setup():
    core.fps = 30
    core.WINDOW_SIZE = [800, 600]
    core.memory("agents", [])
    core.memory("items", [])
    core.memory("creeps", [])
    core.memory("obstacles", [])
    for g in range(0, nbGroupes):
        for i in range(0, nbAgents):
            core.memory("agents").append(Agent(groupe=g))
    # core.memory("agents").append(Agent(etat=Etat.CONTAGIEUX))
    for i in range(0, nbCreeps):
        core.memory("creeps").append(Creep())

    for i in range(0, nbObstacles):
        core.memory("obstacles").append(Obstacle())


def run():
    core.cleanScreen()
    for agent in core.memory("agents"):
        agent.computePerception()
        agent.compteDecision()
        agent.show()

    if core.getMouseLeftClick():
        agent = getClosestAgent(core.getMouseLeftClick())
        agent.body.etat = Etat.INCUBATION
        agent.body.delai = Epidemie.dureeIncubation.value

    # print sum of state of agents
    print("Sains: %d, Contagieux: %d, Immunes: %d, Mort: %d" % (
        len([a for a in core.memory("agents") if a.body.etat == Etat.SAIN]),
        len([a for a in core.memory("agents") if a.body.etat == Etat.CONTAGIEUX]),
        len([a for a in core.memory("agents") if a.body.etat == Etat.IMMUNISE]),
        len([a for a in core.memory("agents") if a.body.etat == Etat.MORT]),
    ))
    for agent in core.memory("creeps"):
        agent.show()

    for obstacle in core.memory("obstacles"):
        obstacle.show()


def getClosestAgent(position=Vector2(0, 0)):
    closestAgent = core.memory("agents")[0]
    for agent in core.memory("agents"):
        if agent.body.position.distance_to(position) < closestAgent.body.position.distance_to(position):
            closestAgent = agent
    return closestAgent


core.main(setup, run)
