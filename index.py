#Import packages
import pygame
from pygame.locals import *
import sys

#Define constants
BLACK = (0,0,0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SEC = 30

#Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

#Load assets



#Initialize variabels



#Loop forever
while True:

    #Check for handle events
    for event in pygame.event.get():

        #Quit program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    #"Per frame" actions

    
   

    #Clear window
    window.fill(BLACK)

    

    #Draw elements



    #Update windows
    pygame.display.update()

    #Slow things down
    clock.tick(FRAMES_PER_SEC)



