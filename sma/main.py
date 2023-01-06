
import core
from sma.agent import Agent
from sma.creep import Creep
from sma.obstacle import Obstacle

nbAgents = 10
nbCreeps = 0
nbObstacles = 0

def setup():
    core.fps = 30
    core.WINDOW_SIZE = [800, 600]
    core.memory("agents", [])
    core.memory("items", [])
    core.memory("creeps", [])
    core.memory("obstacles", [])
    for i in range(0, nbAgents):
        core.memory("agents").append(Agent())

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

    for agent in core.memory("creeps"):
        agent.show()

    for obstacle in core.memory("obstacles"):
        obstacle.show()






core.main(setup, run)
