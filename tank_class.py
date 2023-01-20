import pygame
from pygame.locals import *
import math

class Tank:
    def __init__(self, window, x, y, angle, image, keyset):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 5
        self.window = window
        self.image = pygame.image.load(image)
        self.rect = pygame.Rect(self.x - int(self.image.get_rect()[2] / 2) , self.y - int(self.image.get_rect()[3] / 2), self.image.get_rect()[2], self.image.get_rect()[3])
        self.keyset = keyset
        self.previous_position = (x, y)

    def update(self, active_keys, obstacles, tanks):
        #Endrer rotasjon
        if active_keys[self.keyset[3]]:
            self.angle -= self.speed
        if active_keys[self.keyset[2]]:
            self.angle += self.speed
        
        #Sjekker om tank er innenfor vinduet og oppdaterer posisjon
        if 0 < self.x < pygame.display.get_surface().get_size()[0] and 0 < self.y < pygame.display.get_surface().get_size()[1]:
            if active_keys[self.keyset[0]]:
                self.previous_position = (self.x, self.y)
                self.x += self.speed * math.cos(self.angle * (math.pi/180))
                self.y += self.speed * -math.sin(self.angle * (math.pi/180))
            if active_keys[self.keyset[1]]:
                self.previous_position = (self.x, self.y)
                self.x += (self.speed-2) * -math.cos(self.angle * (math.pi/180))
                self.y += (self.speed-2) * math.sin(self.angle * (math.pi/180))
        elif pygame.display.get_surface().get_size()[0] < self.x + int(self.image.get_width()):
            self.x -=1
        elif self.x - int(self.image.get_width()) < 0:
            self.x +=1
        elif pygame.display.get_surface().get_size()[1] < self.y:
            self.y -=1
        elif self.y < 0:
            self.y +=1
        
        self.rect = pygame.Rect(self.x - int(self.image.get_rect()[2] / 2) , self.y - int(self.image.get_rect()[3] / 2), self.image.get_rect()[2], self.image.get_rect()[3])

        #Test for kollisjon med hindringer og tanks
        for (obstacle, tank) in zip(obstacles, tanks):
            if self.rect.colliderect(obstacle.rect):
                self.x = self.previous_position[0]
                self.y = self.previous_position[1]

            if tank.rect == self.rect:
                pass
            elif self.rect.colliderect(tank.rect):
                self.x = self.previous_position[0]
                self.y = self.previous_position[1]



    def draw(self):
        #Lager en kopi av tank bildet rotert og tegner det i vinduet
        image_copy = pygame.transform.rotate(self.image, self.angle)
        self.window.blit(image_copy,
        (self.x - int(image_copy.get_width() / 2),
         self.y - int(image_copy.get_height() / 2)))


