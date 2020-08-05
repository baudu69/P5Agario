import inspect
import time
from typing  import cast
from types import FrameType

import pygame

runfuntion = None
setupfunction = None
screen = None
fps = 60
noloop = False
WINDOW_SIZE = [100, 100]

def noLoop():
    global noloop
    noloop = True


def setup():
    pygame.init()
    global WINDOW_SIZE
    WINDOW_SIZE
    if (setupfunction is not None):
        setupfunction()


    global screen
    screen = pygame.display.set_mode(WINDOW_SIZE)

    # Set title of screen
    pygame.display.set_caption("Window")


def run():
    if (runfuntion is not None):
        runfuntion()




def main(setupf,runf):
    print(inspect.stack()[1].function)
    global runfuntion
    runfuntion = runf
    global setupfunction
    setupfunction = setupf

    setup()

    clock = pygame.time.Clock()


    done = False
    while not done:
        if not noloop :
            screen.fill(0)
            run()

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

        clock.tick(fps)

        # Go ahead and update the screen with what we 've drawn.
        pygame.display.flip()


