import pygame
from pygame.locals import *

SCREENRECT = Rect(0, 0, 640, 480)

class Player(pygame.sprite.Sprite):
    lives = 3
    speed = 10
    bounce = 12
    gun_offset = -11
    images = []

    def __init__(self, screen_rectangle):
        pygame.sprite.Sprite.__init__(self, self.containers)

        SCREENRECT = screen_rectangle

        self.image = self.images[0]
        
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.reloding = 0
        self.origtop = self.rect.top
        
        self.facing = -1
        
    def update(self):
        self.rect.move_ip(self.facing, 0)

        if not SCREENRECT.contains(self.rect):
            self.facing = -self.facing
            self.rect.top = self.rect.bottom + 1
            self.rect = self.rect.clamp(SCREENRECT)
        
        self.frame = self.frame + 1
        self.image = self.images[self.frame//self.animation_cycle % 3]
            