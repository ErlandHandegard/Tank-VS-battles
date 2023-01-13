#Import packages
import pygame
from pygame.locals import *
import sys

#Define constants
BLACK = (0,0,0)
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500
FRAMES_PER_SEC = 30
BACKGROUND_IMAGE = pygame.image.load("./visuals/game_background.png")

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
    window.blit(BACKGROUND_IMAGE, (0,0))

    

    #Draw elements



    #Update windows
    pygame.display.update()

    #Slow things down
    clock.tick(FRAMES_PER_SEC)



