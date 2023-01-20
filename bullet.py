import pygame
from pygame.locals import *
import math

class Bullet:
    def __init__(self, window, x, y, angle):
        self.image = pygame.image.load(".\visuals\PNG\Default size\bulletDark3_outline.png")
        self.speed = 10
        self.window = window
        self.angle = angle
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.image.get_rect()[2], self.image.get_rect()[3])

    def bullet(self, obstacles, tanks):
        flying = True
        while flying:
            self.x += self.speed * math.cos(self.angle * (math.pi/180))
            self.y += self.speed * -math.sin(self.angle * (math.pi/180))

            if self.x > pygame.display.get_surface().get_size()[0] or self.x < 0:
                del self
            elif self.y > 0 or self.y < pygame.display.get_surface().get_size()[1]:
                del self

            for tank in tanks:
                if self.rect.colliderect(tank.ract):
                    #Slette tanken bulleten og sette score eventuelt skape en eksplosjon
                    flying = False

    
            for obstacle in obstacles:
                if self.rect.colliderect(obstacle.rect):
                    #Slette instansen eventluelt lage en eksposjon
                    flying = False

