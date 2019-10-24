import pygame
from pygame.locals import *

class PlayerLives(pygame.sprite.Sprite):
    lives = 3  # player lives

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.font = pygame.font.Font(None, 20)
        self.font.set_italic(1)
        self.color = Color('white')
        self.last_lives = -1
        self.update()
        self.rect = self.image.get_rect().move(850, 5)

    def update(self):
        if self.lives != self.last_lives:
            self.last_lives = self.lives
            msg = "Lives: %d" % self.lives
            self.image = self.font.render(msg, 0, self.color)

