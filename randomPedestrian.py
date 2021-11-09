import random
import pygame
from pygame.math import Vector2
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
    core.memory("origine", Vector2(200, 400))
    core.memory("positionVecteur",Vector2(0,0))
    core.memory("monVecteur",Vector2(0,200))
    core.memory("magnitude",core.memory("monVecteur").magnitude())
    print("Setup END-----------")


def run():

    core.cleanScreen()

    if core.getKeyPressList(276):
        if core.memory("monVecteur").angle_to(Vector2(0,1)) > -45:
            core.memory("monVecteur", core.memory("monVecteur").rotate(1))
    elif core.getKeyPressList(275):
        if core.memory("monVecteur").angle_to(Vector2(0, 1)) < 45:
            core.memory("monVecteur", core.memory("monVecteur").rotate(-1))
    else:
        if abs(core.memory("monVecteur").angle_to(Vector2(0,1)))>0.00001:
            if core.memory("monVecteur").angle_to(Vector2(0,1)) < 0:
                core.memory("monVecteur", core.memory("monVecteur").rotate(-1))
            else:
                core.memory("monVecteur", core.memory("monVecteur").rotate(1))

    if core.getKeyPressList(273):
        core.memory("monVecteur", core.memory("monVecteur").scale_to_length(core.memory("monVecteur").magnitude()+10))
    elif core.getKeyPressList(274) and core.memory("monVecteur").magnitude()>10:
        core.memory("monVecteur", core.memory("monVecteur").scale_to_length(core.memory("monVecteur").magnitude()-10))
    else:
        if core.memory("monVecteur").magnitude() != core.memory("magnitude"):

            if abs(core.memory("monVecteur").magnitude() - core.memory("magnitude")) > 0.0001:
                if core.memory("monVecteur").magnitude() - core.memory("magnitude") < 0 :
                    core.memory("monVecteur", core.memory("monVecteur").scale_to_length(core.memory("monVecteur").magnitude()+ 10))
                else:
                    core.memory("monVecteur", core.memory("monVecteur").scale_to_length(core.memory("monVecteur").magnitude() - 10))


    pygame.draw.line(core.screen,(255,255,255),core.memory("origine")+core.memory("positionVecteur"),core.memory("origine")+ Vector2(core.memory("monVecteur").x,-core.memory("monVecteur").y))

core.main(setup, run)
