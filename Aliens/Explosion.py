import pygame
from pygame.locals import *
import random

class Explosion(pygame.sprite.Sprite):
    defaultlife = 12
    animation_cycle = 3
    images = []

    def __init__(self, actor):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=actor.rect.center)

        self.life = self.defaultlife

    def update(self):
        self.life = self.life - 1

        self.image = self.frame + 1
        self.image = self.images[self.life//self.animation_cycle % 2]
        
        if self.life <= 0:
            self.kill()
            