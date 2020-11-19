import random

import pygame
import core

hauteur = 500
largeur = 500

balls = []  #  [ [x,y,xdir,ydir],[x2,y2,xDir2,yDir2].... ]

def setup():
    print("setup")
    global balls
    core.WINDOW_SIZE=[hauteur,largeur]
    core.fps=30

    for i in range(0,10):
        x = random.randint(0,largeur)
        y = random.randint(0,hauteur)

        xd = random.uniform(-5,5)
        yd = random.uniform(-5, 5)
        balls = balls + [ [ x ,y ,xd,yd ] ]


def run():
    print("Run")

    #Affichage
    for b in balls:
        print(b)
        pygame.draw.circle(core.screen, (255, 0, 0), (b[0],b[1]), 20)


    #Update Position
    for b in balls:
        b[0] = b[0] + b[2]
        b[1] = b[1] + b[3]

    #Gestion des bords de l'écran

core.main(setup,run)


