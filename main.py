#Import packages
import pygame
from pygame.locals import *
import sys
from tank_class import *
from obstacle import *
from bullet import *

#Define constants

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

tank = Tank(window, 50, WINDOW_HEIGHT / 2, 0, "./visuals/PNG/Default size/tank_blue.png",  (K_w, K_s, K_a, K_d, K_c))
tank2 = Tank(window, WINDOW_WIDTH - 50, WINDOW_HEIGHT / 2, 180, "./visuals/PNG/Default size/tank_green.png", (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_m))

crate = Obstacle(window, 500, 300, "./visuals/PNG/Default size/crateWood.png")
tree = Obstacle(window, 800, 200, "./visuals/PNG/Default size/treeGreen_large.png" )

tanks = [tank, tank2]
obstacles = [crate, tree]
bullets = []


#Loop forever
while True:

    #Check for handle events
    for event in pygame.event.get():

        #Quit program
        if event.type == pygame.QUIT:
            print(bullets)
            pygame.quit()
            sys.exit()


    active_keys = pygame.key.get_pressed()

    #"Per frame" actions
    
    tank.update(active_keys, obstacles, tanks, bullets)
    tank2.update(active_keys, obstacles, tanks, bullets)


    for bullet in bullets:
        bullet.update(obstacles, tanks, bullets)


    #Clear window
    window.blit(BACKGROUND_IMAGE, (0,0))



    #Draw elements
    for bullet in bullets:
        bullet.draw()

    tank.draw()
    tank2.draw()
    for bullet in bullets:
        bullet.draw()

    for obstacle in obstacles:
        obstacle.draw()
    
    

    #Update windows
    pygame.display.update()

    #Slow things down
    clock.tick(FRAMES_PER_SEC)
