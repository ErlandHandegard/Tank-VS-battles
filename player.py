import pygame
from pygame.locals import *


class Player:
    def __init__(self, window, tank, position):
        self.tank = tank
        self.window = window
        self.position = position


    def draw(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(str(10-self.tank.hits_taken), True, (0, 0, 128))
        self.window.blit(text, self.position)
