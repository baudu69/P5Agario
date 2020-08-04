import random
import pygame
from pygame.rect import Rect

import core


def setup():
    print("Setup")
    core.fps = 1

def run():

    pygame.draw.circle(core.screen,(255, 255, 255),(200,200),100,1)
    pygame.draw.rect(core.screen,(0, 255, 0),Rect((100, 100), (200, 200)),1)

    count = 0
    for i in range(0,10000):
        x = random.uniform(100, 300)
        y = random.uniform(100, 300)

        dist = (200-x)*(200-x)+(200-y)*(200-y)

        if dist < 100*100 :
            pygame.draw.circle(core.screen, (0, 0, 255), (int(x), int(y)), 2, 1)
            count+=1
        else :
            pygame.draw.circle(core.screen, (255, 0, 0), (int(x), int(y)), 2, 1)

    pi = float(4 * count/10000.0)
    print("PI : ", pi)




core.main(setup,run)


