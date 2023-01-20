import pygame
from pygame.locals import *

class Player:
    def __init__(self):
        self.score = 0
        self.tank = Tank(window, 50, WINDOW_HEIGHT / 2, 0, "./visuals/PNG/Default size/tank_blue.png",  (K_w, K_s, K_a, K_d, K_c))