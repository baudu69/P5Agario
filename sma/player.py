import core
from sma.agent import Agent


class Player(Agent):
    def show(self):
        core.Draw.circle((255, 0, 0), (self.body.position.x, self.body.position.y), 30, 0)