import pygame
import core


def setup():
    print("Setup")

def run():
    print("run")
    pygame.draw.circle(core.screen,(255, 255, 255),(200,200),100,3)




core.main(setup,run)


