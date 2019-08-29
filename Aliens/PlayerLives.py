import pygame
from pygame.locals import *

LIVES = 3  # player lives

class PlayerLives(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.font = pygame.font.Font(None, 20)
        self.font.set_italic(1)
        self.color = Color('white')
        self.last_lives = -1
        self.update()
        self.rect = self.image.get_rect().move(60, 450)

    def update(self):
        if LIVES != self.last_lives:
            self.last_lives = LIVES
            msg = "Lives: %d" % LIVES
            self.image = self.font.render(msg, 0, self.color)

