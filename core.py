import inspect
import time
from typing  import cast
from types import FrameType

import pygame

runfuntion = None
setupfunction = None
screen = None



def setup():
    pygame.init()
    WINDOW_SIZE = [400, 400]
    global screen
    screen = pygame.display.set_mode(WINDOW_SIZE)

    # Set title of screen
    pygame.display.set_caption("Map")
    if(setupfunction is not None):
        setupfunction()

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
        run()
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

        clock.tick(60)

        # Go ahead and update the screen with what we 've drawn.
        pygame.display.flip()


