import pygame
from pygame.locals import *

class Obstacle():
    def __init__(self, window, x, y, image):
        self.window = window
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.rect = pygame.Rect(self.x, self.y, self.image.get_rect()[2], self.image.get_rect()[3])
        print(self.rect.midbottom)

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

