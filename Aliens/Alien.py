import pygame
from pygame.locals import *
import random

class Alien(pygame.sprite.Sprite):
    speed = 13
    animation_cycle = 12
    images = []
    
    def __init__(self, screen_rectangle):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.SCREENRECT = screen_rectangle
        
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.facing = random.choice((-1, 1)) * self.speed
        self.frame = 0
        
        if self.facing < 0:
            self.rect.right = self.SCREENRECT.right
    
    def update(self):
        self.rect.move_ip(self.facing, 0)

        if not self.SCREENRECT.contains(self.rect):
            self.facing = -self.facing
            self.rect.top = self.rect.bottom + 1
            self.rect = self.rect.clamp(self.SCREENRECT)
        
        self.frame = self.frame + 1
        self.image = self.images[self.frame//self.animation_cycle % 3]
            