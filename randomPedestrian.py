import random
import pygame
from pygame.math import Vector2
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 600]
    core.memory("origine", Vector2(400, 600))
    core.memory("positionVecteur", Vector2(0, 0))
    core.memory("vecteurAcceleration", Vector2(0, 200))
    core.memory("magnitude", core.memory("vecteurAcceleration").magnitude())

    core.memory("bobPosition", Vector2(50, 200))
    core.memory("bobOrientation", 0)

    print("Setup END-----------")


def run():
    core.cleanScreen()
    if core.getKeyPressList(pygame.K_r):
        core.memory("origine", Vector2(400, 600))
        core.memory("positionVecteur", Vector2(0, 0))
        core.memory("vecteurAcceleration", Vector2(0, 200))
        core.memory("magnitude", core.memory("vecteurAcceleration").magnitude())

        core.memory("bobPosition", Vector2(0, 200))
        core.memory("bobOrientation", 0)

    if core.getKeyPressList(pygame.K_LEFT):
        if core.memory("vecteurAcceleration").angle_to(Vector2(0, 1)) > -45:
            core.memory("vecteurAcceleration", core.memory("vecteurAcceleration").rotate(1))
    elif core.getKeyPressList(pygame.K_RIGHT):
        if core.memory("vecteurAcceleration").angle_to(Vector2(0, 1)) < 45:
            core.memory("vecteurAcceleration", core.memory("vecteurAcceleration").rotate(-1))
    else:
        if abs(core.memory("vecteurAcceleration").angle_to(Vector2(0, 1))) > 0.00001:
            if core.memory("vecteurAcceleration").angle_to(Vector2(0, 1)) < 0:
                core.memory("vecteurAcceleration", core.memory("vecteurAcceleration").rotate(-1))
            else:
                core.memory("vecteurAcceleration", core.memory("vecteurAcceleration").rotate(1))

    if core.getKeyPressList(pygame.K_UP):
        core.memory("vecteurAcceleration", core.memory("vecteurAcceleration").scale_to_length(core.memory("vecteurAcceleration").magnitude() + 10))
    elif core.getKeyPressList(pygame.K_DOWN) and core.memory("vecteurAcceleration").magnitude() > 10:
        core.memory("vecteurAcceleration", core.memory("vecteurAcceleration").scale_to_length(core.memory("vecteurAcceleration").magnitude() - 10))
    else:
        if abs(core.memory("vecteurAcceleration").magnitude() - core.memory("magnitude")) > 10:
            if core.memory("vecteurAcceleration").magnitude() - core.memory("magnitude") < 0:
                core.memory("vecteurAcceleration",
                            core.memory("vecteurAcceleration").scale_to_length(core.memory("vecteurAcceleration").magnitude() + 10))
            else:
                core.memory("vecteurAcceleration",
                            core.memory("vecteurAcceleration").scale_to_length(core.memory("vecteurAcceleration").magnitude() - 10))

    # Controle de Bobo
    core.memory("bobOrientation", core.memory("bobOrientation") + core.memory("vecteurAcceleration").angle_to(Vector2(0, 1)))
    core.memory("bobPosition", core.memory("bobPosition")+core.memory("vecteurAcceleration").rotate(-core.memory("bobOrientation")).normalize()*(core.memory("vecteurAcceleration").magnitude()-core.memory("magnitude"))/10)

    if core.memory("bobPosition").x < core.memory("origine").x-core.WINDOW_SIZE[0]:
        core.memory("bobPosition", Vector2(10+core.memory("origine").x-core.WINDOW_SIZE[0],core.memory("bobPosition").y))
    if core.memory("bobPosition").x > core.WINDOW_SIZE[0]-core.memory("origine").x:
        core.memory("bobPosition", Vector2(core.WINDOW_SIZE[0]-core.memory("origine").x-10,core.memory("bobPosition").y))
    if core.memory("bobPosition").y > core.WINDOW_SIZE[1]:
        core.memory("bobPosition", Vector2(core.memory("bobPosition").x,core.WINDOW_SIZE[1]-10))
    if core.memory("bobPosition").y < core.WINDOW_SIZE[1] - core.memory("origine").y:
        core.memory("bobPosition", Vector2(core.memory("bobPosition").x, core.WINDOW_SIZE[1] - core.memory("origine").y + 20))


    # Draw vect
    pygame.draw.line(core.screen, (255, 255, 255), core.memory("origine") + core.memory("positionVecteur"),
                     core.memory("origine") + Vector2(core.memory("vecteurAcceleration").x, -core.memory("vecteurAcceleration").y))

    drawBob()


def drawBob():
    p1 = core.memory("bobPosition") + Vector2(-5, 0).rotate(180-core.memory("bobOrientation"))
    p1.y = -p1.y
    p1 = p1 + core.memory("origine")
    p2 = core.memory("bobPosition") + Vector2(0, -15).rotate(180-core.memory("bobOrientation"))
    p2.y = -p2.y
    p2 = p2 + core.memory("origine")
    p3 = core.memory("bobPosition") + Vector2(5, 0).rotate(180-core.memory("bobOrientation"))
    p3.y = -p3.y
    p3 = p3 + core.memory("origine")

    pygame.draw.polygon(core.screen, (255, 0, 0), ((p1), (p2), (p3)))


core.main(setup, run)
