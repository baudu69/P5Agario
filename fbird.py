import random
import time

import pygame
from pygame.math import Vector2
import core


gravity=5
player = [100,200]
obstaclesHaut = []
obstaclesBas = []
score = 0
gameOver=False
bg = None

def setup():
    print("Setup START---------")
    global obstaclesHaut, obstaclesBas, score, bg

    bg = pygame.image.load("bg.png")

    score = time.time()
    core.fps = 30
    core.WINDOW_SIZE = [600, 400]

    for i in range(0,10):
        x = random.randint(80,200)


        obstaclesHaut = obstaclesHaut + [[300+i*80,0,40,200-x/2]]
        obstaclesBas = obstaclesBas + [[300 + i * 80, 200+x/2, 40, 400]]

    print("Setup END-----------")



def is_in(player, obstacle):
    #rect : X,Y,Largeur,Hauteur
    xRectHaut = obstacle[0]
    yRectHaut =  obstacle[1]
    xRectBas = obstacle[0]+obstacle[3]
    yRectBas = obstacle[1]+obstacle[2]

    if player[0] > xRectBas and player[1] < yRectBas or  player[0] > xRectBas and player[1] > yRectBas:
        return True


def run():

    #UPDATE
    global player,gameOver,score



    if gameOver != True:
        print('score :' + str(int(time.time() - score)))
        player[1]+=gravity

        for obstacle in obstaclesHaut:
            obstacle[0]-=1
            if obstacle[0] == 0:
                obstacle[0]=600
        for obstacle in obstaclesBas:
            obstacle[0]-=1
            if obstacle[0] == 0:
                obstacle[0]=600

        if core.mouseclickL:
            player[1]-=15

        if player[1]>400:
            gameOver=True

            #Colision
        for obstacle in obstaclesHaut:
            if is_in(player, obstacle):
                gameOver=True

        for obstacle in obstaclesBas:
            if is_in(player, obstacle):
                gameOver=True

    #DRAW
    core.screen.blit(bg,(0,0))
    pygame.draw.circle(core.screen,(255,0,0),(player[0],player[1]),20)

    for obstacle in obstaclesHaut:
        pygame.draw.rect(core.screen,(0,255,0),(obstacle[0],obstacle[1],obstacle[2],obstacle[3]))
    for obstacle in obstaclesBas:
        pygame.draw.rect(core.screen,(0,255,0),(obstacle[0],obstacle[1],obstacle[2],obstacle[3]))
core.main(setup, run)
