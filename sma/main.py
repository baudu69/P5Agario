# import random
# from pygame.math import Vector2
# import core
#
#
# def setup():
#     print("Setup START---------")
#     core.fps = 30
#     core.WINDOW_SIZE = [400, 400]
#
#     core.memory("agents", [])
#     core.memory("item", [])
#
#     print("Setup END-----------")
#
#
# def computePerception(agent):
#     pass
#
#
# def computeDecision(agent):
#     pass
#
#
# def applyDecision(agent):
#     pass
#
#
# def run():
#     core.cleanScreen()
#
#     #Display
#     for agent in core.memory("agents"):
#         agent.show()
#
#     for item in core.memory("item"):
#         item.show()
#
#     for agent in core.memory("agents"):
#         computePerception(agent)
#
#     for agent in core.memory("agents"):
#         computeDecision(agent)
#
#     for agent in core.memory("agents"):
#         applyDecision(agent)
#
#
#
#
#
# core.main(setup, run)
from pygame import Vector2

import core
from sma.agent import Agent
from sma.body import Body
from sma.creep import Creep
from sma.player import Player
from sma.fustrom import Fustrom





def setup():
    core.fps = 30
    core.WINDOW_SIZE = [800, 600]
    core.memory("agents", [])
    core.memory("items", [])
    core.memory("creeps", [])
    for i in range(0, 30):
        core.memory("agents").append(Agent())

    for i in range(0, 50):
        core.memory("creeps").append(Creep())


def run():
    core.cleanScreen()
    for agent in core.memory("agents"):
        agent.computePerception()
        agent.compteDecision()
        agent.show()

    for agent in core.memory("creeps"):
        agent.show()






core.main(setup, run)
