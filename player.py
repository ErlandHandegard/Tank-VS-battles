import pygame
from pygame.locals import *

class Player:
    def __init__(self, tank):
        self.tank = tank
        self.lives = 10
    
    def update(self):
        if self.tank.hit():
            self.s