import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    lives = 3
    speed = 10
    bounce = 12
    gun_offset = -11
    images = []

    def __init__(self, screen_rectangle):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.SCREENRECT = screen_rectangle

        self.image = self.images[0]
        
        self.rect = self.image.get_rect(midbottom=self.SCREENRECT.midbottom)
        self.reloading = 0
        self.origtop = self.rect.top
        
        self.facing = -1
        
    def move(self, direction):
        if (direction is not None):
            self.facing = direction

        self.rect.move_ip(self.facing * self.speed, 0)

        self.rect = self.rect.clamp(self.SCREENRECT)

        if self.facing < 0:
         self.image = self.images[0]
        elif self.facing > 0:
            self.image = self.images[1]

        self.rect.top = self.origtop - (self.rect.left//self.bounce % 2)

    def gunpos(self):
        gun_position = self.facing*self.gun_offset + self.rect.centerx

        return gun_position, self.rect.top
        
