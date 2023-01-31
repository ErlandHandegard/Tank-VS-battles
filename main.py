#Import packages
import pygame
from pygame.locals import *
import sys
from tank_class import *
from obstacle import *
from bullet import *
from player import *

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

player1 = Player(window,tank, (25, 25))
player2 = Player(window,tank2, (WINDOW_WIDTH - 55, 25))

crate = Obstacle(window, 500, 300, "./visuals/PNG/Default size/crateWood.png")
tree = Obstacle(window, 800, 200, "./visuals/PNG/Default size/treeGreen_large.png" )
barrel = Obstacle(window, 200, 200, "./visuals/PNG/Default size/barrelBlack_top.png" )

tanks = [tank, tank2]
obstacles = [crate, tree, barrel]
bullets = []

def re_initialize_players():
    global tank
    global tank2

    global player1
    global player2

    tank = Tank(window, 50, WINDOW_HEIGHT / 2, 0, "./visuals/PNG/Default size/tank_blue.png",  (K_w, K_s, K_a, K_d, K_c))
    tank2 = Tank(window, WINDOW_WIDTH - 50, WINDOW_HEIGHT / 2, 180, "./visuals/PNG/Default size/tank_green.png", (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_m))

    player1 = Player(window,tank, (25, 25))
    player2 = Player(window,tank2, (WINDOW_WIDTH - 55, 25))


#Loop forever
while True:

    #Check for handle events
    for event in pygame.event.get():

        #Quit program
        if event.type == pygame.QUIT:
            print(bullets)
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_position = pygame.mouse.get_pos()


    active_keys = pygame.key.get_pressed()

    #"Per frame" actions
    
    tank.update(active_keys, obstacles, tanks, bullets)
    tank2.update(active_keys, obstacles, tanks, bullets)

    

    for bullet in bullets:
        bullet.update(obstacles, tanks, bullets)


    

    #Clear window
    window.blit(BACKGROUND_IMAGE, (0,0))


    #Draw elements
    player1.draw()
    player2.draw()

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
