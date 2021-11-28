import random
import threading
import time

import pygame
from pygame.math import Vector2, Vector3
import core


def swap(array, i, j):
    c = array[i]
    array[i]=array[j]
    array[j]=c


def partition(array, start, end):
    pivotIndex = start
    pivotValue=array[end]
    for i in range(start,end):
        if array[i]<pivotValue:
            swap(array,i,pivotIndex)
            pivotIndex+=1
    swap(array,pivotIndex,end)
    return pivotIndex


def quicksort(array,start,end):
    if core.memory("stop"):
        return
    if start >= end:
        return
    index = partition(array,start,end)
    time.sleep(0.02)
    quicksort(array,start,index-1)
    quicksort(array, index+1, end)


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 600]


    core.memory("nb", int(800/6))
    core.memory("array", [i for i in range(0,core.memory("nb"))])

    random.shuffle(core.memory("array"))
    core.memory("stop",False)
    core.memory("thread",threading.Thread(target=quicksort, args=(core.memory("array"),0,len(core.memory("array"))-1)))
    core.memory("thread").start()


    print("Setup END-----------")


def run():
    core.cleanScreen()
    if core.getKeyPressList(pygame.K_r):
        reset()
    if core.getKeyPressList(pygame.K_q):
        core.memory("stop",True)


    for i,v in enumerate(core.memory("array")):
        rect = [i*5+i,600-600*v/160,5,600*v/160]
        pygame.draw.rect(core.screen,(255,255,255),rect)

def reset():
    core.memory("stop", True)
    core.memory("array", [i for i in range(0, core.memory("nb"))])

    random.shuffle(core.memory("array"))
    core.memory("stop", False)
    core.memory("thread",threading.Thread(target=quicksort, args=(core.memory("array"), 0, len(core.memory("array")) - 1)))
    core.memory("thread").start()

core.main(setup, run)
